# restore_working_github.ps1
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$gitConfigPath = "$env:USERPROFILE\.gitconfig"
if (Test-Path $gitConfigPath) {
    Remove-Item $gitConfigPath
    Write-Output ".gitconfig removed"
} else {
    Write-Output ".gitconfig not found"
}

git config --global user.email "popkovdaniil66@gmail.com"
git config --global user.name "DaniilPopkov"

$url = "https://github.com/DaniilPopkov/WorldBooks.git"

echo "url=$url" | git credential reject

Write-Output "The script was executed successfully!"

