
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, RichLog, Input
from textual.binding import Binding


class GPTConsole(App):
    """a basic GPT console example"""
    TITLE = "GPT Console"
    BINDINGS = [Binding(key="q", action="quit_gpt_console", description="Quit App"),
                Binding(key="c", action="clear_gpt_console", description="Clear Console"),]
    CSS_PATH = "console-tui.tcss"

    def compose(self) -> ComposeResult:
        yield Header(name=self.TITLE, show_clock=False)
        yield Input(placeholder=f"Send a message")
        yield RichLog(highlight=True, markup=True)
        yield Footer()

    def on_mount(self):
        pass

    @on(Input.Submitted)
    async def input_submitted(self, message: Input.Submitted) -> None:
        await self.ask_gpt(f"{message.value}")

    async def ask_gpt(self, message):
        # input gpt4all here
        self.query_one(RichLog).write(f"[bold magenta] {message}")
        self.query_one(RichLog).write(f"[bold aliceblue] {message}")
    
    def action_clear_gpt_console(self) -> None:
        self.query_one(RichLog).clear()

    def action_quit_gpt_console(self) -> None:
        self.app.exit()

if __name__ == "__main__":
    app = GPTConsole()
    app.run()