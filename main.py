from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
from fpdf import FPDF
import io

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ GPT AI Assistant Webhook đang hoạt động."

@app.route("/software/guide", methods=["POST"])
def software_guide():
    data = request.json
    return jsonify({
        "huong_dan": f"Hướng dẫn sử dụng phần mềm {data.get('phan_mem', '...')} cho mục tiêu: {data.get('muc_tieu', '...')}."
    })

@app.route("/marketing/report", methods=["POST"])
def marketing_report():
    data = request.json
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    content = f"Báo cáo Marketing:\n\nPhần mềm: {data.get('phan_mem')}\nMục tiêu: {data.get('muc_tieu')}"
    pdf.multi_cell(0, 10, content)
    pdf_path = "/tmp/marketing_report.pdf"
    pdf.output(pdf_path)
    return send_file(pdf_path, as_attachment=True)

@app.route("/dashboard/create", methods=["POST"])
def dashboard_create():
    data = request.json
    values = data.get("data", [5, 10, 15])
    plt.figure(figsize=(5, 3))
    plt.plot(values, marker="o")
    plt.title("Biểu đồ mẫu")
    img_path = "/tmp/dashboard.png"
    plt.savefig(img_path)
    return send_file(img_path, mimetype="image/png")

if __name__ == "__main__":
    app.run()
