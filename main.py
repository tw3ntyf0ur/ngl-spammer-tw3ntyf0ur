#NGL Spammer - Fsociety

import requests
import threading
import time
import random
import json
import socket
import socks
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.table import Table
from rich import box
from fake_useragent import UserAgent
from stem import Signal
from stem.control import Controller

class NGLOperationShadowV99:
    """
    SHADOW MODE V99: PERFECT DELIVERY SYSTEM
    Intelligent delays with advanced stealth capabilities
    """
    
    def __init__(self, target_username: str, max_workers: int = 3):
        self.target_username = target_username
        self.target_url = f"https://ngl.link/api/submit"
        self.max_workers = max_workers
        self.request_count = 0
        self.success_count = 0
        self.fail_count = 0
        self.rate_limit_count = 0
        self.lock = threading.Lock()
        self.console = Console()
        self.start_time = None
        self.last_request_time = 0
        self.min_delay = 1.0  # Increased minimum delay for better stealth
        self.max_delay = 2.0  # Increased maximum delay
        
        # Enhanced user-agent rotation with real-time generation
        self.ua_generator = UserAgent()
        
        # Advanced message pool with contextual variations
        self.message_pool = self.generate_advanced_message_pool()
        
        # Proxy configuration
        self.proxy_list = self.load_proxies()
        self.use_tor = False
        self.tor_control_port = 9051
        self.tor_proxy = "socks5://127.0.0.1:9050"
        
        # Session management for connection persistence
        self.session = requests.Session()
        self.session.trust_env = False  # Prevent using system proxies accidentally
        
    def load_proxies(self):
        """Load proxies from file if available"""
        try:
            with open('proxies.txt', 'r') as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            return []
    
    def rotate_tor_ip(self):
        """Rotate TOR IP address for enhanced anonymity"""
        try:
            with Controller.from_port(port=self.tor_control_port) as controller:
                controller.authenticate()
                controller.signal(Signal.NEWNYM)
                self.console.print("[yellow]🔄 TOR IP rotated successfully[/yellow]")
        except Exception as e:
            self.console.print(f"[red]⚠ TOR rotation failed: {e}[/red]")
    
    def generate_advanced_message_pool(self) -> list:
        """Generate comprehensive message pool with contextual variations"""
        base_messages = [
            "just turn it off, bro", "why even make that?", "attention seeker much",
            "so cringe omg", "stop acting busy", "you serious with this?", 
            "such a tryhard lol", "way too extra man", "what's the point of this",
            "totally useless tbh", "just fishing for clout", "old trick, so lame",
            "nobody cares anyway", "when will you grow up?", "same lame style again",
            "so nosy, bro", "skip, waste of data", "straight up trash", 
            "that trend's dead soon", "get a real hobby", "desperate for attention",
            "not even original", "seen this a million times", "zero creativity",
            "embarrassing honestly", "try something new", "cringe level over 9000"
        ]
        
        # Add some variations with different formats
        variations = []
        for msg in base_messages:
            variations.extend([
                msg,
                msg.upper(),
                msg.capitalize(),
                msg + "!",
                msg + "??",
                msg + " :)",
                msg + " :(",
                msg + " smh"
            ])
        
        return variations
    
    def get_random_user_agent(self):
        """Generate fresh user agent for each request"""
        return self.ua_generator.random
    
    def intelligent_delay(self):
        """Smart delay system with adaptive timing based on server response"""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        # Adaptive delay based on recent failures
        adaptive_delay = self.min_delay
        if self.rate_limit_count > 0:
            adaptive_delay += self.rate_limit_count * 0.5
        
        if time_since_last < adaptive_delay:
            sleep_time = adaptive_delay - time_since_last
            time.sleep(sleep_time)
        
        # Add randomized extra delay for human-like behavior
        extra_delay = random.uniform(0.8, 2.2)
        time.sleep(extra_delay)
        
        self.last_request_time = time.time()
    
    def get_proxy(self):
        """Get a random proxy or TOR configuration"""
        if self.use_tor:
            return {'http': self.tor_proxy, 'https': self.tor_proxy}
        elif self.proxy_list:
            proxy = random.choice(self.proxy_list)
            return {'http': proxy, 'https': proxy}
        return None
    
    def generate_payload(self, message: str) -> dict:
        """Craft precision payload for NGL API with randomized parameters"""
        return {
            'question': message,
            'username': self.target_username,
            'deviceId': f'shadow_{random.randint(1000000000, 9999999999)}_{int(time.time())}',
            'gameSlug': '',
            'referrer': '',
            'timestamp': str(int(time.time() * 1000))
        }
    
    def execute_single_strike(self, message: str, attempt: int = 1) -> tuple:
        """Execute request with intelligent delay and advanced retry logic"""
        if attempt > 3:  # Max 3 attempts
            return False, "MAX ATTEMPTS REACHED"
        
        # Intelligent delay before each request
        self.intelligent_delay()
        
        headers = {
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://ngl.link',
            'Referer': f'https://ngl.link/{self.target_username}',
            'X-Requested-With': 'XMLHttpRequest',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'trailers'
        }
        
        try:
            payload = self.generate_payload(message)
            proxy_config = self.get_proxy()
            
            response = self.session.post(
                self.target_url,
                data=payload,
                headers=headers,
                timeout=12,
                proxies=proxy_config,
                allow_redirects=True,
                verify=True  # SSL verification to appear legitimate
            )
            
            with self.lock:
                self.request_count += 1
                
                if response.status_code == 200:
                    try:
                        response_data = response.json()
                        if 'questionId' in response_data:
                            self.success_count += 1
                            return True, f"SUCCESS: {response_data['questionId'][:8]}..."
                        else:
                            # Retry on unusual 200 response
                            time.sleep(2.0)
                            return self.execute_single_strike(message, attempt + 1)
                    except:
                        self.success_count += 1
                        return True, "SUCCESS (Non-JSON)"
                elif response.status_code == 429:
                    self.fail_count += 1
                    self.rate_limit_count += 1
                    # Increase delay and potentially rotate IP
                    self.min_delay += 1.2
                    if self.use_tor and attempt == 1:
                        self.rotate_tor_ip()
                    time.sleep(3.0)
                    return self.execute_single_strike(message, attempt + 1)
                else:
                    self.fail_count += 1
                    return False, f"HTTP {response.status_code}"
                    
        except requests.exceptions.RequestException as e:
            # Network error, retry with increased delay
            time.sleep(2.0)
            return self.execute_single_strike(message, attempt + 1)
        except Exception as e:
            self.fail_count += 1
            return False, f"ERROR: {str(e)}"
    
    def display_banner(self):
        """Show operation banner with enhanced details"""
        banner = Panel.fit(
            f"[bold red]Tw3ntyF0ur[/bold red]\n"
            f"[white]PERFECT DELIVERY SYSTEM v2.0[/white]\n\n"
            f"[yellow]Target:[/yellow] [cyan]{self.target_username}[/cyan]\n"
            f"[yellow]Messages:[/yellow] [cyan]{len(self.message_pool)} variations[/cyan]\n"
            f"[yellow]Stealth Level:[/yellow] [green]MAXIMUM[/green]\n"
            f"[yellow]Anonymity:[/yellow] [green]{'TOR + Proxies' if self.use_tor and self.proxy_list else 'TOR' if self.use_tor else 'Proxies' if self.proxy_list else 'Standard'}[/green]\n"
            f"[yellow]Delay:[/yellow] [green]{self.min_delay}-{self.max_delay}s[/green]",
            box=box.DOUBLE,
            title="[blink]STEALTH MODE ACTIVATED[/blink]",
            border_style="red"
        )
        self.console.print(banner)
    
    def get_stats_table(self) -> Table:
        """Return enhanced statistics table"""
        if self.start_time is None:
            return Table()
            
        elapsed = time.time() - self.start_time
        rate = self.request_count / elapsed if elapsed > 0 else 0
        
        table = Table(show_header=True, header_style="bold magenta", box=box.ROUNDED)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_column("Rate", style="yellow")
        
        table.add_row("Total Requests", str(self.request_count), f"{rate:.2f}/sec")
        success_rate = (self.success_count/self.request_count*100) if self.request_count > 0 else 0
        table.add_row("Successful", str(self.success_count), f"{success_rate:.1f}%")
        table.add_row("Failed", str(self.fail_count), "N/A")
        table.add_row("Rate Limits", str(self.rate_limit_count), "N/A")
        table.add_row("Elapsed Time", f"{elapsed:.2f}s", "N/A")
        table.add_row("Stealth Level", "MAXIMUM", "N/A")
        
        return table
    
    def launch_assault(self, total_attacks: int):
        """Initiate assault with perfect delivery system"""
        self.start_time = time.time()
        self.last_request_time = time.time()
        
        self.display_banner()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=self.console
        ) as progress:
            task = progress.add_task("[red]Executing stealth delivery...", total=total_attacks)
            
            # Use controlled threading for optimal performance
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = []
                
                for i in range(total_attacks):
                    message = random.choice(self.message_pool)
                    futures.append(executor.submit(self.execute_single_strike, message))
                    
                    # Small delay between task submissions
                    time.sleep(0.2)
                
                # Process results as they complete
                for future in as_completed(futures):
                    success, result = future.result()
                    progress.update(task, advance=1)
                    
                    if success:
                        progress.console.print(f"[green]✓ {result}[/green]")
                    else:
                        progress.console.print(f"[red]✗ {result}[/red]")
        
        # Display results
        self.console.print("\n")
        stats_table = self.get_stats_table()
        
        final_panel = Panel(
            stats_table,
            title="[bold red]MISSION COMPLETED[/bold red]",
            border_style="green",
            box=box.DOUBLE
        )
        
        self.console.print(final_panel)
        
        # Success analysis
        if self.success_count == total_attacks:
            self.console.print("\n[bold green]🎯 PERFECT DELIVERY! 100% SUCCESS RATE![/bold green]")
            self.console.print(f'''\n[bold green]               
                    .ed"""" """$$$$be.
                   -"           ^""**$$$e.
                 ."                   '$$$c
                /                      "4$$b
               d  3                      $$$$
               $  *                   .$$$$$$
              .$  ^c           $$$$$e$$$$$$$$.
              d$L  4.         4$$$$$$$$$$$$$$b
              $$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
  e$""=.      $$$$P d$$$$F $ $$$$$$$$$- $$$$$$
 z$$b. ^c     3$$$F "$$$$b   $"$$$$$$$  $$$$*"      .=""$c
4$$$$L        $$P"  "$$b   .$ $$$$$...e$$        .=  e$$$.
^*$$$$$c  %..   *c    ..    $$ 3$$$$$$$$$$eF     zP  d$$$$$
  "**$$$ec   "   %ce""    $$$  $$$$$$$$$$*    .r" =$$$$P""
        "*$b.  "c  *$e.    *** d$$$$$"L$$    .d"  e$$***"
          ^*$$c ^$c $$$      4J$$$$$% $$$ .e*".eeP"
             "$$$$$$"'$=e....$*$$**$cz$$" "..d$*"
               "*$$$  *=%4.$ L L$ P3$$$F $$$P"
                  "$   "%*ebJLzb$e$$$$$b $P"
                    %..      4$$$$$$$$$$ "
                     $$$e   z$$$$$$$$$$%
                      "*$c  "$$$$$$$P"
                       ."""*$$$$$$$$bc
                    .-"    .$***$$$"""*e.
                 .-"    .e$"     "*$c  ^*b.
          .=*""""    .e$*"          "*bc  "*$e..
        .$"        .z*"               ^*$e.   "*****e.
        $$ee$c   .d"                     "*$.        3.
        ^*$E")$..$"                         *   .ee==d%
           $.d$$$*                           *  J$$$e*
            """""                              "$$$" ''')
            self.console.print("[bold white]tw3ntyf0ur mission accomplished![/bold white]")
    
        elif self.success_count > 0:
            self.console.print(f"\n[green]✅ Delivery completed: {self.success_count}/{total_attacks} messages[/green]")

def main():
    """Main execution function."""
    console = Console()
    
    intro_banner = Panel.fit(
        """[bold red] 
 ███▄    █   ▄████  ██▓         ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
 ██ ▀█   █  ██▒ ▀█▒▓██▒       ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
▓██  ▀█ ██▒▒██░▄▄▄░▒██░       ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
▓██▒  ▐▌██▒░▓█  ██▓▒██░         ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
▒██░   ▓██░░▒▓███▀▒░██████▒   ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░▓  ░   ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░░   ░ ▒░  ░   ░ ░ ░ ▒  ░   ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
   ░   ░ ░ ░ ░   ░   ░ ░      ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
         ░       ░     ░  ░         ░                 ░  ░       ░          ░      ░  ░   ░     
                                                                                                
        [/bold red]\n"""
        "[bold red]🩸👁️‍🗨️ Fsociety v2.0[/bold red]\n"
        "[white]ADVANCED STEALTH DELIVERY SYSTEM[/white]\n\n"
        "[bold white]made by tw3ntyf0ur[/bold white]\n"
        "[yellow]Features:[/yellow] TOR Support + Proxy Rotation + Adaptive Timing\n"
        "[yellow]Success Rate:[/yellow] Optimized for maximum stealth delivery",
        box=box.HEAVY,
        border_style="red"
    )
    console.print(intro_banner)
    
    # Get user input
    console.print("\n")
    target_username = console.input("[bold yellow]🎯 Enter Target NGL Username: [/bold yellow]")
    total_attacks = int(console.input("[bold yellow]💣 Enter Total Messages to Send [15]: [/bold yellow]") or "15")
    
    # Initialize operation
    operation = NGLOperationShadowV99(target_username=target_username, max_workers=2)
    
    # Configure advanced options
    use_tor = console.input("[bold cyan]🌐 Use TOR? (y/N): [/bold cyan]").lower() == 'y'
    if use_tor:
        operation.use_tor = True
        console.print("[green]✓ TOR enabled[/green]")
    
    # Confirm
    console.print("\n")
    confirm_panel = Panel(
        f"[red]Target:[/red] [white]{target_username}[/white]\n"
        f"[red]Messages:[/red] [white]{total_attacks} to send[/white]\n"
        f"[red]Strategy:[/red] [green]STEALTH MODE + INTELLIGENT TIMING[/green]\n"
        f"[red]Anonymity:[/red] [green]{'TOR + Proxies' if operation.use_tor and operation.proxy_list else 'TOR' if operation.use_tor else 'Proxies' if operation.proxy_list else 'Standard'}[/green]\n"
        f"[red]Expected Time:[/red] [white]~{total_attacks * 5}s[/white]",
        title="[blink]CONFIRM STEALTH DELIVERY[/blink]",
        border_style="yellow"
    )
    console.print(confirm_panel)
    
    confirmation = console.input("[bold red]🚀 Launch operation? (y/N): [/bold red]")
    if confirmation.lower() != 'y':
        console.print("[yellow]Operation cancelled.[/yellow]")
        return
    
    # Execute
    console.print("\n")
    try:
        operation.launch_assault(total_attacks)
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Operation interrupted[/yellow]")
    except Exception as e:
        console.print(f"\n[red]❌ Critical error: {e}[/red]")

if __name__ == "__main__":
    main()