from .ImageGeneratorImg2img import ImageGeneratorImg2img
from .ImageGeneratorTxt2img import ImageGeneratorTxt2img

NODE_CLASS_MAPPINGS = {
    "aigate_img2img": ImageGeneratorImg2img,
    "aigate_txt2img": ImageGeneratorTxt2img,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "aigate_img2img": "全能图片-图生图",
    "aigate_txt2img": "全能图片-文生图",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
