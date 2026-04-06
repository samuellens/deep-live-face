<div align="center">

# DeepFaceLive

**Real-time face swap for PC streaming or video calls**

![DeepFaceLive](doc/deepfacelive_intro.png)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![ONNX](https://img.shields.io/badge/ONNX-Runtime-green.svg)](https://onnxruntime.ai/)
[![DirectX12](https://img.shields.io/badge/DirectX-12-orange.svg)](https://docs.microsoft.com/en-us/windows/win32/direct3d12/direct3d-12-graphics)
[![Discord](https://img.shields.io/badge/Discord-Join-7289DA.svg)](https://discord.gg/rxa7h9M6rH)

![ONNX](doc/logo_onnx.png) ![DirectX](doc/logo_directx.png) ![Python](doc/logo_python.png)

</div>

---

## Table of Contents

- [Features](#features)
- [Face Swap (DFM)](#face-swap-dfm)
- [Face Swap (Insight)](#face-swap-insight)
- [Face Animator](#face-animator)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Releases](#releases)
- [Contributing](#contributing)
- [Community](#community)
- [Support the Project](#support-the-project)

---

## Features

- **Real-time Face Swapping** - Swap faces in live video streams or recordings
- **Multiple Face Models** - Choose from pre-trained models or train your own
- **Webcam Support** - Use your webcam for live face swapping
- **Video Processing** - Process pre-recorded videos
- **Face Animation** - Control static face pictures using video input
- **Cross-platform** - Windows 10 primary, Linux experimental

---

## Face Swap (DFM)

Swap your face from a webcam or video using trained face models (DeepFaceLab Model format).

> **Note:** These persons do not exist. Any similarities with real people are purely coincidental. Except Keanu Reeves. He exists, and he's breathtaking!

### Available Face Models

<table align="center">
<tr>
<td align="center">
<strong>Keanu Reeves</strong><br>
<img src="doc/celebs/Keanu_Reeves/Keanu_Reeves.png" width="128"><br>
<a href="doc/celebs/Keanu_Reeves/examples.md">examples</a>
</td>
<td align="center">
<strong>Irina Arty</strong><br>
<img src="doc/celebs/Irina_Arty/Irina_Arty.png" width="128"><br>
examples
</td>
<td align="center">
<strong>Millie Park</strong><br>
<img src="doc/celebs/Millie_Park/Millie_Park.png" width="128"><br>
examples
</td>
<td align="center">
<strong>Rob Doe</strong><br>
<img src="doc/celebs/Rob_Doe/Rob_Doe.png" width="128"><br>
<a href="doc/celebs/Rob_Doe/examples.md">examples</a>
</td>
<td align="center">
<strong>Jesse Stat</strong><br>
<img src="doc/celebs/Jesse_Stat/Jesse_Stat.png" width="128"><br>
examples
</td>
</tr>
<tr>
<td align="center">
<strong>Bryan Greynolds</strong><br>
<img src="doc/celebs/Bryan_Greynolds/Bryan_Greynolds.png" width="128"><br>
<a href="doc/celebs/Bryan_Greynolds/examples.md">examples</a>
</td>
<td align="center">
<strong>Mr. Bean</strong><br>
<img src="doc/celebs/Mr_Bean/Mr_Bean.png" width="128"><br>
examples
</td>
<td align="center">
<strong>Ewon Spice</strong><br>
<img src="doc/celebs/Ewon_Spice/Ewon_Spice.png" width="128"><br>
<a href="doc/celebs/Ewon_Spice/examples.md">examples</a>
</td>
<td align="center">
<strong>Natasha Former</strong><br>
<img src="doc/celebs/Natasha_Former/Natasha_Former.png" width="128"><br>
<a href="doc/celebs/Natasha_Former/examples.md">examples</a>
</td>
<td align="center">
<strong>Emily Winston</strong><br>
<img src="doc/celebs/Emily_Winston/Emily_Winston.png" width="128"><br>
<a href="doc/celebs/Emily_Winston/examples.md">examples</a>
</td>
</tr>
<tr>
<td align="center">
<strong>Ava de Addario</strong><br>
<img src="doc/celebs/Ava_de_Addario/Ava_de_Addario.png" width="128"><br>
<a href="doc/celebs/Ava_de_Addario/examples.md">examples</a>
</td>
<td align="center">
<strong>Dilraba Dilmurat</strong><br>
<img src="doc/celebs/Dilraba_Dilmurat/Dilraba_Dilmurat.png" width="128"><br>
examples
</td>
<td align="center">
<strong>Matilda Bobbie</strong><br>
<img src="doc/celebs/Matilda_Bobbie/Matilda_Bobbie.png" width="128"><br>
<a href="doc/celebs/Matilda_Bobbie/examples.md">examples</a>
</td>
<td align="center">
<strong>Yohanna Coralson</strong><br>
<img src="doc/celebs/Yohanna_Coralson/Yohanna_Coralson.png" width="128"><br>
<a href="doc/celebs/Yohanna_Coralson/examples.md">examples</a>
</td>
<td align="center">
<strong>Amber Song</strong><br>
<img src="doc/celebs/Amber_Song/Amber_Song.png" width="128"><br>
examples
</td>
</tr>
<tr>
<td align="center">
<strong>Kim Jarrey</strong><br>
<img src="doc/celebs/Kim_Jarrey/Kim_Jarrey.png" width="128"><br>
<a href="doc/celebs/Kim_Jarrey/examples.md">examples</a>
</td>
<td align="center">
<strong>David Kovalniy</strong><br>
<img src="doc/celebs/David_Kovalniy/David_Kovalniy.png" width="128"><br>
<a href="doc/celebs/David_Kovalniy/examples.md">examples</a>
</td>
<td align="center">
<strong>Jackie Chan</strong><br>
<img src="doc/celebs/Jackie_Chan/Jackie_Chan.png" width="128"><br>
examples
</td>
<td align="center">
<strong>Nicola Badge</strong><br>
<img src="doc/celebs/Nicola_Badge/Nicola_Badge.png" width="128"><br>
<a href="doc/celebs/Nicola_Badge/examples.md">examples</a>
</td>
<td align="center">
<strong>Joker</strong><br>
<img src="doc/celebs/Joker/Joker.png" width="128"><br>
examples
</td>
</tr>
<tr>
<td align="center">
<strong>Dean Wiesel</strong><br>
<img src="doc/celebs/Dean_Wiesel/Dean_Wiesel.png" width="128"><br>
<a href="doc/celebs/Dean_Wiesel/examples.md">examples</a>
</td>
<td align="center">
<strong>Silwan Stillwone</strong><br>
<img src="doc/celebs/Silwan_Stillwone/Silwan_Stillwone.png" width="128"><br>
<a href="doc/celebs/Silwan_Stillwone/examples.md">examples</a>
</td>
<td align="center">
<strong>Tim Chrys</strong><br>
<img src="doc/celebs/Tim_Chrys/Tim_Chrys.png" width="128"><br>
<a href="doc/celebs/Tim_Chrys/examples.md">examples</a>
</td>
<td align="center">
<strong>Zahar Lupin</strong><br>
<img src="doc/celebs/Zahar_Lupin/Zahar_Lupin.png" width="128"><br>
<a href="doc/celebs/Zahar_Lupin/examples.md">examples</a>
</td>
<td align="center">
<strong>Tim Norland</strong><br>
<img src="doc/celebs/Tim_Norland/Tim_Norland.png" width="128"><br>
<a href="doc/celebs/Tim_Norland/examples.md">examples</a>
</td>
</tr>
<tr>
<td align="center">
<strong>Natalie Fatman</strong><br>
<img src="doc/celebs/Natalie_Fatman/Natalie_Fatman.png" width="128"><br>
<a href="doc/celebs/Natalie_Fatman/examples.md">examples</a>
</td>
<td align="center">
<strong>Liu Lice</strong><br>
<img src="doc/celebs/Liu_Lice/Liu_Lice.png" width="128"><br>
<a href="doc/celebs/Liu_Lice/examples.md">examples</a>
</td>
<td align="center">
<strong>Albica Johns</strong><br>
<img src="doc/celebs/Albica_Johns/Albica_Johns.png" width="128"><br>
<a href="doc/celebs/Albica_Johns/examples.md">examples</a>
</td>
<td align="center">
<strong>Meggie Merkel</strong><br>
<img src="doc/celebs/Meggie_Merkel/Meggie_Merkel.png" width="128"><br>
<a href="doc/celebs/Meggie_Merkel/examples.md">examples</a>
</td>
<td align="center">
<strong>Tina Shift</strong><br>
<img src="doc/celebs/Tina_Shift/Tina_Shift.png" width="128"><br>
<a href="doc/celebs/Tina_Shift/examples.md">examples</a>
</td>
</tr>
</table>

> **Want higher quality?** Train your own face model using [DeepFaceLab](https://github.com/iperov/DeepFaceLab). Check out this [example](https://www.tiktok.com/@arnoldschwarzneggar/video/6995538782204300545) of Arnold Schwarzenegger trained for video calls.

---

## Face Swap (Insight)

Swap your face using just a **single photo** - no training required!

<div align="center">
<img src="doc/lukashenko.png" width="128">
<br><br>
<img src="doc/insight_faceswap_example.gif">
</div>

---

## Face Animator

Control a static face picture using video or your webcam. Perfect for creating funny videos, memes, or real-time streaming at 25 FPS (requires ~35 TFLOPS GPU).

<div align="center">
<img src="doc/face_animator_example.gif">
</div>

### Demo

[![Stranger Things Theme Intro Acapella](doc/Ng1C78Ceyxg_screenshot.png)](https://www.youtube.com/watch?v=Ng1C78Ceyxg)

> **Tutorial:** Watch this [mini video](doc/FaceAnimator_tutor.webm?raw=true) showing how to set up Face Animator (Obama controlling Kim Jong-un's face).

---

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **GPU** | DirectX 12 compatible | RTX 2070+ / RX 5700 XT+ |
| **CPU** | Modern CPU with AVX | - |
| **RAM** | 4GB | 8GB+ |
| **Paging File** | 32GB+ | 32GB+ |
| **OS** | Windows 10 | Windows 10/11 |

---

## Installation

### Windows (Recommended)

Download the latest release - no installation required:

1. Download from [Yandex.Disk](https://disk.yandex.ru/d/7i5XTKIKVg5UUg) or [MEGA](https://mega.nz/folder/m10iELBK#Y0H6BflF9C4k_clYofC7yA)
2. Extract the self-extracting archive
3. Run the application

**Available Builds:**
- **DirectX12 Build** - Works with NVIDIA, AMD, and Intel GPUs
- **NVIDIA Build** - NVIDIA only (GT730+), faster than DX12

### Linux

See [Build Instructions](build/linux) for Linux installation.

---

## Usage

### Basic Usage

```bash
# Run DeepFaceLive
python main.py run DeepFaceLive

# Run with custom userdata directory
python main.py run DeepFaceLive --userdata-dir ~/deepface_data

# Run without CUDA (CPU only)
python main.py run DeepFaceLive --no-cuda
```

### Training

```bash
# Train FaceAligner model
python main.py train FaceAligner --workspace-dir ./workspace --faceset-path ./data.dfs
```

### Development Utilities

```bash
# Split large files for distribution
python main.py dev split_large_files

# Merge split files
python main.py dev merge_large_files --delete-parts

# Extract FaceSynthetics dataset
python main.py dev extract_FaceSynthetics --input-dir ./FaceSynthetics --faceset-path ./output.dfs
```

### Command-Line Options

```bash
python main.py --help          # Show help
python main.py --version       # Show version
python main.py --verbose       # Enable verbose logging
```

---

## Documentation

### Setup Guides

| Platform | Guide |
|----------|-------|
| **Windows** | [Main Setup](doc/windows/main_setup.md) |
| | [Streaming Setup](doc/windows/for_streaming.md) |
| | [Video Calls Setup](doc/windows/for_video_calls.md) |
| | [Using Android Phone Camera](doc/windows/using_android_phone_camera.md) |
| **Linux** | [Build Info](build/linux) |

### FAQ

- [User FAQ](doc/user_faq/user_faq.md)
- [Developer FAQ](doc/developer_faq/developer_faq.md)

---

## Releases

| Platform | Download | Notes |
|----------|----------|-------|
| Windows 10 x64 | [Yandex.Disk](https://disk.yandex.ru/d/7i5XTKIKVg5UUg) | Zero-dependency portable build |
| Windows 10 x64 | [MEGA](https://mega.nz/folder/m10iELBK#Y0H6BflF9C4k_clYofC7yA) | Mirror download |

---

## Contributing

We welcome contributions! Here's how you can help:

1. **Train Face Models** - Follow the FAQ recommendations and share quality models on Discord
2. **Report Issues** - Submit bug reports and feature requests
3. **Submit PRs** - Code improvements, documentation fixes, etc.
4. **Star the Repo** - Show your support!

---

## Community

| Platform | Link | Description |
|----------|------|-------------|
| **Discord** | [Join Server](https://discord.gg/rxa7h9M6rH) | Official channel (English/Russian) |
| **QQ Group** | 124500433 | Chinese community |

---

## Support the Project

If you find DeepFaceLive useful, consider supporting development:

- **Yoomoney:** [Donate](https://yoomoney.ru/to/41001142318065)
- **Bitcoin:** `bc1qewl062v70rszulml3f0mjdjrys8uxdydw3v6rq`

---

<div align="center">

**Made with deep learning**

</div>
