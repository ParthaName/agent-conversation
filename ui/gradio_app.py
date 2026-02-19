import gradio as gr
from orchestrator.conversation_manager import run_conversation_stream


def start_discussion(topic):
    for history, status in run_conversation_stream(topic):
        yield history, status


with gr.Blocks() as demo:
    gr.Markdown("# Multi-Agent AI Discussion")

    topic_input = gr.Textbox(label="Enter Topic")
    start_btn = gr.Button("Start Discussion")

    conversation_output = gr.Textbox(label="Conversation", lines=20)
    status_output = gr.Textbox(label="Analysis / Status")

    start_btn.click(
        start_discussion,
        inputs=topic_input,
        outputs=[conversation_output, status_output]
    )

demo.launch()