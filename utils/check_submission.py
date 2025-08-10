def check_submission(lab_name, submission):
	lab_name = lab_name.strip().lower()
	submission = submission.strip()
	if lab_name == 'lab 1: introduction to python':
		# Accepts any print statement with Hello, World!
		if ("print('Hello, World!')" in submission or
			'print("Hello, World!")' in submission or
			'print(\'Hello, World!\')' in submission or
			'print(\"Hello, World!\")' in submission):
			return 'Correct!'
		else:
			return 'Try again.'
	elif lab_name == 'lab 2: data structures':
		# Example: check if the user defines a list or dict (very basic)
		if 'list' in submission or '[' in submission or 'dict' in submission or '{' in submission:
			return 'Correct!'
		else:
			return 'Try again.'
	else:
		return 'Lab not recognized.'
