import torch
import torchxrayvision as xrv
from torchvision import transforms
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# pytorch-grad-cam関連のモジュールをインポート
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image

# 1. TorchXRayVisionの事前学習済みモデルをロード
# "densenet121-res224-all"はChestX-ray14等複数のデータセットで学習されたモデル
model = xrv.models.DenseNet(weights="densenet121-res224-all")
model.eval()  # 推論モードへ

# 2. サンプルX線画像の読み込み
# ※NIH ChestX-ray14等の公開データセットから取得した画像ファイルのパスを指定してください
img_path = "00000001_000.png"
img = Image.open(img_path).convert("L")  # 画像はグレースケール（1チャネル）

# 3. 画像の前処理（モデルが要求する224x224サイズ、正規化）
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

input_tensor = transform(img).unsqueeze(0)  # バッチサイズ1に展開
input_tensor = (input_tensor - 0.5) * 1000


# 4. 推論実施
output = model(input_tensor)
# TorchXRayVisionモデルでは出力は疾患ごとのスコア（各疾患に対するlogit値）になっています
pathologies = model.pathologies  # 対象となる疾患リスト
predictions = {pathologies[i]: output[0, i].item() for i in range(len(pathologies))}

print("=== 疾患予測スコア ===")
for disease, score in predictions.items():
    print(f"{disease}: {score:.4f}")

# 5. Grad-CAMの計算
# 今回はモデル内部の最終畳み込み層を対象とします。TorchXRayVisionのDenseNetの場合、
# 例えば"model.features.denseblock4.denselayer16.conv2"（バージョンにより異なる場合あり）を利用可能です。
target_layer = model.features.denseblock4.denselayer16.conv2

# GradCAMインスタンスの生成（GPU使用可否を自動判定）
cam = GradCAM(model=model, target_layers=[target_layer])

# Grad-CAM計算：入力画像に対し勾配情報からヒートマップを生成
grayscale_cam = cam(input_tensor=input_tensor)
grayscale_cam = grayscale_cam[0, :]  # バッチサイズ1なので先頭を抽出

# 6. 入力画像にヒートマップを重ねて可視化
# 入力画像を[0,1]の範囲に変換し、3チャネルに展開
input_image = np.array(img.resize((224, 224))) / 255.0
if len(input_image.shape) == 2:
    input_image = np.repeat(input_image[..., np.newaxis], 3, axis=-1)

visualization = show_cam_on_image(input_image, grayscale_cam, use_rgb=True)

# 7. 結果の表示
plt.figure(figsize=(10, 5))

plt.subplot(1,2,1)
plt.imshow(input_image, cmap='gray')
plt.title("input")
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(visualization)
plt.title("Grad-CAM")
plt.axis('off')

plt.tight_layout()
plt.show()
plt.savefig("cam.png")