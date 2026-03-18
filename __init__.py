from .ImageGeneratorImg2img import ImageGeneratorImg2img
from .ImageGeneratorTxt2img import ImageGeneratorTxt2img
from .SettingsNode import SettingsNode

NODE_CLASS_MAPPINGS = {
    "setting": SettingsNode,
    "aigate_img2img": ImageGeneratorImg2img,
    "aigate_txt2img": ImageGeneratorTxt2img,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "setting": "设置API key",
    "aigate_txt2img": "全能图片-文生图",
    "aigate_img2img": "全能图片-图生图",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
