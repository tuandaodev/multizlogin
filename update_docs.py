import sys

filepath = 'src/views/api-doc.ejs'

try:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Authentication section
    auth_section = """
    <hr/>

    <h2>🔒 Xác thực (Authentication)</h2>
    <p>Tất cả các API dưới đây đều yêu cầu xác thực bằng API Key. Bạn phải truyền API Key qua Header của request bằng một trong các phương thức sau:</p>
    <ul>
        <li><code>x-api-key: YOUR_API_KEY</code></li>
        <li><code>Authorization: Bearer YOUR_API_KEY</code></li>
    </ul>
    <p>Nếu không có API Key hợp lệ, server sẽ trả về mã lỗi <code>401 Unauthorized</code>.</p>
"""
    
    if "Xác thực (Authentication)" not in content:
        # Find where to insert: before '<!-- ===== ACCOUNT MANAGEMENT APIs ===== -->'
        target = '<!-- ===== ACCOUNT MANAGEMENT APIs ===== -->'
        content = content.replace(target, auth_section + '\n    ' + target)
    
    # Update curl commands
    content = content.replace('curl http://', 'curl -H "x-api-key: YOUR_API_KEY" http://')
    content = content.replace('curl -X POST -H "Content-Type: application/json"', 'curl -X POST -H "x-api-key: YOUR_API_KEY" -H "Content-Type: application/json"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Documentation updated successfully.")
except Exception as e:
    print(f"Error: {e}")
