import pyzipper
import webbrowser
import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

# Initialize Rich Console
console = Console()
today = datetime.now()

# Banner with exact styling
logo = Panel.fit(
    f"""[bold green]

┏━┓╻ ╻   ┏━╸┏━┓┏━┓┏━╸╻┏ 
┣━┛┗┳┛   ┃  ┣┳┛┣━┫┃  ┣┻┓
╹   ╹    ┗━╸╹┗╸╹ ╹┗━╸╹ ╹

[navy_blue]|[bold white] Author: [bold green]@STARK-404[/bold green]|[navy_blue] [bold white]Github: [bold green]@STARK-404 [navy_blue]|[bold green] {today.strftime("%d/%m/%Y")}|

""",
    border_style="bold blue"
)

def extract_zip_with_password(zip_path, extract_path='PyCrack.zip'):
    """
    Extract a password-protected zip file using pyzipper.
    If password is wrong, redirect to payment page.
    """
    
    # Display banner
    console.print(logo)
    
    # Check if the zip file exists
    if not os.path.exists(zip_path):
        console.print(f"[bold red]Error: Zip file '{zip_path}' not found.[/bold red]")
        return False
    
    console.print(f"[bold cyan]🔐 Attempting to extract: {zip_path}[/bold cyan]")
    console.print("=" * 60)
    
    while True:
        # Get password from user
        password = console.input("[bold yellow]Enter the password for the zip file: [/bold yellow]")
        
        try:
            # Try to extract with the provided password
            with pyzipper.AESZipFile(zip_path, 'r') as zip_file:
                zip_file.setpassword(password.encode('utf-8'))
                zip_file.extractall(extract_path)
                
            console.print(f"\n[bold green]✅ Success! Files extracted to: {os.path.abspath(extract_path)}[/bold green]")
            console.print("[bold green]🎉 Extraction completed successfully![/bold green]")
            return True
            
        except RuntimeError as e:
            # Wrong password error
            if "Bad password" in str(e) or "password" in str(e).lower():
                console.print("\n[bold red]❌ Wrong password![/bold red]")
                
                # Create a styled panel for the message
                message_panel = Panel.fit(
                    """[bold yellow]
╔══════════════════════════════════════════════════════════════╗
║  Buy the password from next page when you click enter!       ║
║  Press enter to be redirected to the payment page.           ║
║  For any enquiries contact the author                        ║
╚══════════════════════════════════════════════════════════════╝
                    """,
                    border_style="bold red",
                    title="[bold red]⚠️ ACCESS DENIED ⚠️[/bold red]",
                    subtitle="[bold yellow]@STARK-404[/bold yellow]"
                )
                console.print(message_panel)
                
                # Wait for user to press Enter
                console.input("[bold cyan]Press Enter to be redirected to the payment page...[/bold cyan]")
                
                # Redirect to payment page
                payment_url = "https://buymeacoffee.com/mrstarkin/e/471721"
                console.print(f"\n[bold green]🌐 Redirecting to: {payment_url}[/bold green]")
                webbrowser.open(payment_url)
                
                # Ask if user wants to try again
                retry = console.input("\n[bold yellow]Do you want to try entering the password again? (yes/no): [/bold yellow]").lower()
                if retry not in ['yes', 'y']:
                    console.print("[bold red]Exiting...[/bold red]")
                    return False
                console.print("\n" + "=" * 60 + "\n")
            else:
                console.print(f"[bold red]Error extracting file: {e}[/bold red]")
                return False
                
        except pyzipper.BadZipFile:
            console.print("[bold red]Error: The file is not a valid zip file.[/bold red]")
            return False
        except Exception as e:
            console.print(f"[bold red]Unexpected error: {e}[/bold red]")
            return False

def main():
    # Display banner at start
    console.print(logo)
    
    console.print("[bold cyan]🔐 Password-Protected ZIP Extractor[/bold cyan]")
    console.print("=" * 60)
    
    # Get zip file path
    zip_file_path = console.input("[bold yellow]Enter the path to the zip file: [/bold yellow]").strip()
    extract_folder = console.input("[bold yellow]Enter extraction folder path (press Enter for current directory): [/bold yellow]").strip()
    
    if not extract_folder:
        extract_folder = '.'
    
    # Extract the zip file
    success = extract_zip_with_password(zip_file_path, extract_folder)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]Operation cancelled by user.[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]An error occurred: {e}[/bold red]")