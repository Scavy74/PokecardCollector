from core.github_manager import GitHubManager


def main():

    github = GitHubManager()

    print("Connexion à GitHub...")

    manifest = github.get_manifest()

    print("\nManifest reçu :\n")

    print(manifest)


if __name__ == "__main__":
    main()
