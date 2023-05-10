import openai
import config
import typer
from rich import print
from rich.table import Table


def main():

    openai.api_key = config.api_key

    print("🗣️ [bold green]ChatGPT API en Python[/bold green]")

    table = Table("Command", "Description")
    table.add_row("exit", "Exit from the app")
    table.add_row("new", "Cut the conversation and create a new one")

    print(table)

    # Using role and content section, we will give it a context that can influence chatgpt's responses.

    context = {"role": "system", 
                "content": "You are a very helpful assistant."}
    messages = [context] 

    while True:

        content = __prompt()

        if content =="new":
            print("☑️ 👍 [bold blue]We started a new chat[/bold blue]")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        # We will give it the response_content so that chatgpt can remember the answer from previous queries

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green] -> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:

    prompt = typer.prompt("\nWhat do you want to talk about❓")

    if prompt == "exit":
        exit = typer.confirm("⛔ Wait, are you sure about that❓")
        if exit:
            print("👋 We look forward to see you again 🫂")
            raise typer.Abort()

        return __prompt()

    return prompt

if __name__ == "__main__":
    typer.run(main)