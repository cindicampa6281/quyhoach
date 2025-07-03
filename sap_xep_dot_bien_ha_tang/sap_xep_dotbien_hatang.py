import os
import json

# Thư mục chứa file JSON và file đầu ra
directory = 'F:/Cong_viec_thuc_tap/task3/dotbien-hatang'
output_file = 'F:/Cong_viec_thuc_tap/task3/output_construction_projects.json'

# Từ khóa cần tìm trong các gói
keywords = ["thi công xây lắp", "thi công xây dựng"]

# Hàm lọc các dự án có từ khóa
def filter_construction_projects(projects):
    filtered_projects = []
    for project in projects:
        dotbien = project.get('dotbien_hatang', '')
        if dotbien and any(keyword.lower() in dotbien.lower() for keyword in keywords):
            filtered_projects.append({
                "bidName": project.get("bidName"),
                "chudautu": project.get("chudautu"),
                "createdBy": project.get("createdBy"),
                "publicDate": project.get("publicDate"),
                "projectName": project.get("projectName"),
                "bidCloseDate": project.get("bidCloseDate"),
                "id_muasamcong": project.get("id_muasamcong"),
                "tongmuc_dautu": project.get("tongmuc_dautu"),
                "bidNamePlanNew": project.get("bidNamePlanNew"),
                "dotbien_hatang": project.get("dotbien_hatang"),
                "link_muasamcong": project.get("link_muasamcong")
            })
    return filtered_projects

# Hàm xử lý file JSON và trích xuất thông tin
def process_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        file_id = os.path.basename(file_path).replace('.json', '')
        # Bỏ qua nếu tên file không phải số nguyên
        if not file_id.isdigit():
            print(f"Bỏ qua file không hợp lệ: {file_path}")
            return None, None
        filtered_projects = filter_construction_projects(data.get('projects', []))
        return file_id, filtered_projects
    except Exception as e:
        print(f"Lỗi đọc {file_path}: {e}")
        return None, None

# Xử lý tất cả file JSON trong thư mục và sắp xếp
def process_and_sort_by_project_count(directory, output_file):
    output_data = []

    # Duyệt qua các file JSON
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            file_id, projects = process_json_file(file_path)
            if file_id is None:
                continue
            if projects:  # Chỉ thêm nếu có dự án phù hợp
                output_data.append({
                    "id": file_id,
                    "matched_projects": projects
                })

    # Sắp xếp theo số lượng matched_projects (giảm dần)
    output_data.sort(key=lambda x: len(x["matched_projects"]), reverse=True)

    # In số lượng dự án cho mỗi id theo thứ tự từ cao đến thấp
    for entry in output_data:
        print(f"Huyện (mã {entry['id']}): {len(entry['matched_projects'])} gói")

    # Ghi vào file JSON theo thứ tự đã sắp xếp
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\nFile JSON đã được tạo tại: {output_file}")

# Thực hiện xử lý và ghi file
process_and_sort_by_project_count(directory, output_file)