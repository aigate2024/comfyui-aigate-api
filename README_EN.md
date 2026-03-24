# ComfyUI-WaaS-API

[中文](README.md) | English

A collection of ComfyUI image generation nodes based on the Yunfei (云扉) API. Includes text-to-image, image-to-image generation, and more.

## Features

This project provides three main nodes to support flexible image generation workflows:

1. **Settings API Key Node** - Manage and configure API credentials
2. **Image Generator - Text to Image** - Generate images from text descriptions
3. **Image Generator - Image to Image** - Generate new images based on reference images

## Installation

### Method 1: Manual Installation

1. Clone this repository into your ComfyUI's `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/CY-CHENYUE/ComfyUI-WaaS-API.git
   ```

2. Enter the project directory and install dependencies:
   ```bash
   cd ComfyUI-WaaS-API
   ```

   If you're using ComfyUI portable version:
   ```bash
   ..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
   ```

   If you're using your own Python environment:
   ```bash
   pip install -r requirements.txt
   ```

3. Restart ComfyUI

### Method 2: Install via ComfyUI Manager

1. Install and open ComfyUI Manager in ComfyUI
2. Search for "WaaS-API" or "Yunfei"
3. Click the install button
4. Restart ComfyUI

## Node Documentation

### 1. Settings API Key

**Purpose**: Configure and save the API key

**Input Parameters**:
- **apiKey** (required): Your Yunfei API key

**Output**:
- **STRUCT** (Structure): A structure containing API key information for use by other nodes

**Usage Notes**:
- Connect this node's output to the `settings` input of text-to-image or image-to-image nodes
- The API key is securely passed to other nodes

---

### 2. Image Generator - Text to Image (aigate_txt2img)

**Purpose**: Generate images from text descriptions

**Input Parameters**:
- **prompt** (required): Image description text, supports both Chinese and English
- **settings** (required): Structure from the "Settings API Key" node
- **model** (required): Select the model to use
- **aspect_ratio** (optional): Image orientation
  - `Free (Free ratio)` - System decides automatically
  - `Landscape` - 16:9 widescreen
  - `Portrait` - 9:16 portrait
  - `Square` - 1:1 square
- **image_size** (optional): Generated image resolution
  - `1K` - Standard quality
  - `2K` - High quality

**Outputs**:
- **image**: Generated image, can be connected to other nodes for further processing
- **API Respond**: Text information containing processing logs and API responses

**Use Cases**:
- Create unique concept art from text descriptions
- Generate illustrations, backgrounds, or design materials
- Quickly prototype visual content

---

### 3. Image Generator - Image to Image (aigate_img2img)

**Purpose**: Generate new images based on reference images, supports multiple references

**Input Parameters**:
- **prompt** (required): Description or modification instructions for the generated image
- **settings** (required): Structure from the "Settings API Key" node
- **model** (required): Select the model to use
- **aspect_ratio** (optional): Same as text-to-image
- **image_size** (optional): Same as text-to-image
- **image1** (required): First reference image
- **image2-image10** (optional): Up to 9 additional reference images

**Outputs**:
- **image**: Generated image
- **API Respond**: Processing logs and API response information

**Multiple Reference Images Feature**:
- Support for up to 10 reference images in a single generation
- Multiple reference images are sent together to the API as style references
- Ideal for scenarios requiring mixed styles or detailed references
- The first image (image1) is required, others are optional

**Use Cases**:
- Generate new images with similar style to reference images
- Image style transfer
- Create variations based on references
- Multi-source material fusion

---

## Getting API Key

1. Visit the official Yunfei API platform
2. Register or sign in to your account
3. Create a new API key in the API key management section
4. Copy the key to the "Settings API Key" node (no need to re-enter repeatedly)

## Project Architecture

```
BaseImageGenerator.py
├── Shared methods
├── API calls
├── Response handling
└── Logging management

ImageGeneratorTxt2img.py (Inherits)
└── Text-to-image specific logic

ImageGeneratorImg2img.py (Inherits)
└── Image-to-image specific logic + multiple image handling

SettingsNode.py
└── API key configuration
```

## Important Notes

- The API may have usage limits or costs, please refer to the official documentation
- Image generation quality and speed depend on API service status and network connection
- Reference images will be sent to the API servers, please be aware of privacy concerns
- API keys are securely transmitted via HTTP Authorization header
- Image orientation is a suggestion parameter; model output may not strictly follow requirements

## File Description

- `BaseImageGenerator.py` - Base class containing all shared methods
- `ImageGeneratorTxt2img.py` - Text-to-image node implementation
- `ImageGeneratorImg2img.py` - Image-to-image node implementation
- `SettingsNode.py` - API key settings node
- `__init__.py` - Node registration and mapping
- `requirements.txt` - Project dependencies

## Contact

- X (Twitter): [@cychenyue](https://x.com/cychenyue)
- TikTok: [@cychenyue](https://www.tiktok.com/@cychenyue)
- YouTube: [@CY-CHENYUE](https://www.youtube.com/@CY-CHENYUE)
- BiliBili: [@CY-CHENYUE](https://space.bilibili.com/402808950)
- Xiaohongshu: [@CY-CHENYUE](https://www.xiaohongshu.com/user/profile/6360e61f000000001f01bda0)

## License

Please refer to the LICENSE file for licensing information
