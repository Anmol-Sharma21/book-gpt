from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.pdf_service import process_pdf
from app.services.rag_service import get_answer

api = Namespace('pdf', description='PDF operations')

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type='file', required=True, help='PDF file')

query_model = api.model('Query', {
    'question': fields.String(required=True, description='Question to ask')
})

@api.route('/upload')
class PDFUpload(Resource):
    @api.expect(upload_parser)
    def post(self):
        """Upload a PDF for processing"""
        args = upload_parser.parse_args()
        pdf_file = args['file']
        if pdf_file.filename.endswith('.pdf'):
            result = process_pdf(pdf_file)
            return {'message': 'PDF processed successfully', 'chunks': len(result)}, 201
        return {'message': 'Invalid file format'}, 400

@api.route('/query')
class PDFQuery(Resource):
    @api.expect(query_model)
    def post(self):
        """Ask a question about the uploaded PDF"""
        data = request.json
        question = data.get('question')
        if not question:
            return {'message': 'Question is required'}, 400
        return get_answer(question)