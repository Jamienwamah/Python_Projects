def lambda_handler(event, context):
    #To check if number is present in the request body
    if 'number' in event['body']:
        try:
            #Parse the number from the request body
            input_number = int(event['body']['number'])
            #Calculate the square
            result = input_number ** 2
            # Return the square
            return {
                'statusCode': 200,
                'body': f'The squareof {input_number} is {result}'
            }
        except ValueError:
            return {
                'statusCode': 400,
                'body': 'Invalid input. Please providea valid number.'
            }
        else:
            return {
                'statusCode': 400,
                'body': 'Please provide a number in the request body.'
            }