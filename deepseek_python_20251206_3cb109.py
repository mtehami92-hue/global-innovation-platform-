from code.python.array_comparison import calculate_array_response

# Calculate and plot array responses
response_grid = calculate_array_response('grid', f0=25, N=60)
response_golden = calculate_array_response('golden', f0=25, N=60)