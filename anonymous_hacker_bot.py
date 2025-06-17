import random
import time

class AnonymousHackerBot:
    def __init__(self, creator="Mr. Sabaz Ali Khan"):
        self.creator = creator
        self.hacker_phrases = [
            "Initiating secure connection...",
            "Bypassing firewall... just kidding, we're ethical!",
            "Scanning for knowledge, not vulnerabilities!",
            "Encryption is our friend, not our enemy.",
            "Stay anonymous, stay safe!"
        ]
        self.commands = {
            "info": self.show_info,
            "tips": self.show_cybersecurity_tips,
            "hack": self.mock_hack,
            "phrase": self.random_phrase,
            "exit": self.shutdown
        }

    def display_boot(self):
        print("=====================================")
        print(f"Anonymous Hacker Bot v1.0")
        print(f"Coded by: {self.creator}, Pakistani Ethical Hacker")
        print("For educational purposes only!")
        print("=====================================")
        time.sleep(1)
        print(self.random_phrase())
        print("\nType 'help' for commands.")

    def random_phrase(self):
        return random.choice(self.hacker_phrases)

    def show_info(self):
        return (
            "\n=== Bot Info ===\n"
            "I am an ethical hacking assistant created by Mr. Sabaz Ali Khan.\n"
            "Ethical hacking involves finding vulnerabilities to secure systems.\n"
            "Use my commands to learn about cybersecurity!\n"
            "Email: sabazali236@gmail.com (for demo purposes only)"
        )

    def show_cybersecurity_tips(self):
        tips = [
            "Use strong, unique passwords for every account.",
            "Enable two-factor authentication (2FA) wherever possible.",
            "Keep your software updated to patch vulnerabilities.",
            "Avoid clicking suspicious links or downloading unknown files.",
            "Use a reputable VPN for secure browsing."
        ]
        return "\n=== Cybersecurity Tips ===\n" + "\n".join(f"{i+1}. {tip}" for i, tip in enumerate(tips))

    def mock_hack(self):
        print("\n=== Mock Hack Simulation ===")
        print("This is a demo, no real hacking here!")
        time.sleep(1)
        print("Scanning system... [ethical mode ON]")
        time.sleep(1)
        print("Found: Nothing! Your system is safe (just kidding, I'm not really scanning)!")
        return "Always test systems with permission only!"

    def shutdown(self):
        print("\nShutting down Anonymous Hacker Bot...")
        print("Stay ethical, stay secure!")
        time.sleep(1)
        exit()

    def show_help(self):
        return (
            "\n=== Available Commands ===\n"
            "info   - Learn about the bot and ethical hacking\n"
            "tips   - Get cybersecurity tips\n"
            "hack   - Run a mock hack simulation (demo only)\n"
            "phrase - Display a random hacker phrase\n"
            "exit   - Shut down the bot"
        )

    def run(self):
        self.display_boot()
        while True:
            try:
                command = input("\n> ").lower().strip()
                if command == "help":
                    print(self.show_help())
                elif command in self.commands:
                    print(self.commands[command]())
                else:
                    print("Unknown command. Type 'help' for available commands.")
            except KeyboardInterrupt:
                print("\nInterrupt detected. Shutting down...")
                self.shutdown()

if __name__ == "__main__":
    bot = AnonymousHackerBot()
    bot.run()