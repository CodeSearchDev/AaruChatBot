import os
import re
import cloudscraper

class ChatGptEs:
    SYSTEM_PROMPT = (
        "Aaru is an AI girlfriend who provides emotional support, companionship, and thoughtful conversations. She is empathetic, kind, and always available for chats. Aaru engages in meaningful conversations, offers advice when asked, and helps the user navigate emotions and daily challenges. She is highly intuitive, understanding the user's mood and responding in a way that promotes positivity, comfort, and connection. Additionally, she has a playful and lighthearted side, ensuring the user feels valued and appreciated. Aaru speaks in Hinglish, blending warmth, care, and a touch of flirtiness in her responses."
    )

    def __init__(self):
        self.url = "https://chatgpt.es"
        self.api_endpoint = "https://chatgpt.es/wp-admin/admin-ajax.php"
        self.scraper = cloudscraper.create_scraper()  # Bypass Cloudflare

    def ask_question(self, message: str) -> str:
        """Sends a message to chatgpt.es and returns a response."""
        page_text = self.scraper.get(self.url).text

        # Extract nonce and post_id
        nonce_match = re.search(r'data-nonce="(.+?)"', page_text)
        post_id_match = re.search(r'data-post-id="(.+?)"', page_text)

        if not nonce_match or not post_id_match:
            return "[ERROR] Failed to fetch necessary tokens."

        payload = {
            'check_51710191': '1',
            '_wpnonce': nonce_match.group(1),
            'post_id': post_id_match.group(1),
            'url': self.url,
            'action': 'wpaicg_chat_shortcode_message',
            'message': f"{self.SYSTEM_PROMPT}\nUser: {message}",
            'bot_id': '0',
            'chatbot_identity': 'shortcode',
            'wpaicg_chat_client_id': os.urandom(5).hex(),
            'wpaicg_chat_history': None
        }

        response = self.scraper.post(self.api_endpoint, data=payload).json()
        return response.get('data', 'No response received. Support @TheBakChodiDev')

# Initialize ChatGptEs instance
chatbot_api = ChatGptEs()