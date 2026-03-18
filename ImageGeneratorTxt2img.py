from .BaseImageGenerator import BaseImageGenerator


class ImageGeneratorTxt2img(BaseImageGenerator):
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True}),
                "api_key": ("STRING", {"default": "", "multiline": False}),
                "model": (
                    [
                        "PRO-低价渠道版",
                        "PRO-官方稳定版",
                        "V2-低价渠道版",
                        "V2-官方稳定版",
                        "gemini-3-pro-image-preview",
                        "gemini-3.1-flash-image-preview",
                    ],
                    {"default": "gemini-3-pro-image-preview"},
                ),
                "aspect_ratio": (
                    [
                        "Free (自由比例)",
                        "Landscape (横屏)",
                        "Portrait (竖屏)",
                        "Square (方形)",
                    ],
                    {"default": "Free (自由比例)"},
                ),
                "image_size": (["1K", "2K"], {"default": "1K"}),
            },
            "optional": {},
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image", "API Respond")
    FUNCTION = "generate_image"
    CATEGORY = "云扉AiGate"

    def generate_image(
        self,
        prompt,
        api_key,
        model,
        aspect_ratio,
        image_size,
    ):
        """生成图像 - 纯文本到图像"""
        # 重置日志消息
        self.log_messages = []

        try:
            # 获取API密钥
            actual_api_key = self.get_api_key(api_key)

            if not actual_api_key:
                error_message = (
                    "错误: 未提供有效的API密钥。请在节点中输入API密钥或确保已保存密钥。"
                )
                self.log(error_message)
                return self.get_error_response(error_message)

            # 设置API请求头
            headers = {
                "Content-Type": "application/json",
            }

            # 构造请求体（仅包含文本提示）
            parts = [{"text": prompt}]

            # 构造API payload
            payload = self.build_api_payload(parts, aspect_ratio, image_size)

            # 根据选择的模型构造API地址
            self.api_base_url = self.api_base_url_template.format(model=model)
            self.log(f"API地址: {self.api_base_url}")

            # 构造带 API key 的完整 URL
            api_url_with_key = f"{self.api_base_url}?key={actual_api_key}"

            # 调用API
            response = self.call_api(api_url_with_key, headers, payload)

            # 检查响应状态
            if response.status_code != 200:
                error_msg = f"API请求失败，状态码: {response.status_code}, 响应: {response.text}"
                print(error_msg)
                return self.get_error_response(error_msg)

            # 解析响应
            response_data = response.json()

            # 响应处理
            print("API响应接收成功，正在处理...")

            # 处理响应
            img_tensor, response_text, model_version = self.process_response(response_data)

            # 检查响应格式
            if response_text is None:
                return self.get_error_response("API返回了空响应或格式错误")

            # 如果没有找到图像，返回空图像和日志
            if img_tensor is None:
                if not response_text:
                    response_text = "API未返回任何图像或文本"
                return self.get_success_response(
                    self.generate_empty_image(512, 512), response_text, model_version
                )

            # 返回成功响应
            return self.get_success_response(img_tensor, response_text, model_version)

        except Exception as e:
            error_message = f"处理过程中出错: {str(e)}"
            self.log(f"Gemini图像生成错误: {str(e)}")
            return self.get_error_response(error_message)
