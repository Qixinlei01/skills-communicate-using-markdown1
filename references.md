

REPO_OWNER="your_username"
REPO_NAME="your_repository"
YOUR_TOKEN="your_personal_access_token"

# 创建文件 references.md 并提交到分支 my-resume
curl -X PUT -H "Authorization: token $YOUR_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  --data '{
    "message": "Add references.md file with conflicting content",
    "committer": {
      "name": "Your Name",
      "email": "your_email@example.com"
    },
    "content": "This is some conflicting content in references.md",
    "branch": "my-resume"
  }' \
  "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/contents/references.md"
