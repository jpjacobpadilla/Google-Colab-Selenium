from IPython.display import display, HTML, Javascript
import threading
import uuid


class Spinner:
    # Initializer accepts a message
    def __init__(self, message: str, done: str):
        self.message = message
        self.done_message = done
        self.stop_event = threading.Event()

    def __enter__(self):
        self.show_spinner(self.message)
        return self

    def __exit__(self, *args, **kwargs):
        self.remove_spinner()

    def show_spinner(self, text):
        self.spinner_id = uuid.uuid4()

        spinner_html = f"""
            <div class="spinner-container">
                <div class="spinner" id="{self.spinner_id}-circle"></div>
                <div class="spinner-text" id="{self.spinner_id}-text">{text}</div>
            </div>
            <style>
                @keyframes spin {{
                    from {{ transform: rotate(0deg); }}
                    to {{ transform: rotate(360deg); }}
                }}

                .spinner-container {{
                    display: flex;
                    align-items: center;
                    margin-bottom: 3px;
                }}

                .spinner {{
                    border: 3px solid rgba(0, 0, 0, 0.1);
                    border-left-color: lightblue;
                    border-radius: 50%;
                    width: 12px;
                    height: 12px;
                    animation: spin 1s linear infinite;
                }}

                .spinner-text {{
                    padding-left: 6px;
                }}
            </style>
        """
        display(HTML(spinner_html))

    def remove_spinner(self):
        js_code = f"""
            const element = document.getElementById("{self.spinner_id}-circle");
            element.style.border = "3px solid limegreen";
            element.style.animation = "none";

            const text = document.getElementById("{self.spinner_id}-text");
            text.innerText = "{self.done_message}";
        """
        display(Javascript(js_code))
