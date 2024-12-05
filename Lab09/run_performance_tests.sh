#!/bin/bash

# Define variables
API_URL="http://127.0.0.1:6000/submit_message"
POST_DATA='{"alias": "user1", "text": "Hello, world!"}'
POST_FILE="post_data.json"
RESULT_FILE="performance_test_results.txt"
CONCURRENT_USERS=(1 10 50 100 500) # Define concurrency levels for testing

# Prepare the environment
echo -e "Starting Performance Tests...\n" > $RESULT_FILE
echo "POST Data: $POST_DATA" > $POST_FILE

# Ensure ApacheBench is installed
if ! command -v ab &> /dev/null; then
  echo "ApacheBench is not installed. Please install it and run this script again."
  exit 1
fi

# Write the POST data to the post_data.json file
echo $POST_DATA > $POST_FILE

# Test Functions

# Test 1: Load Testing
echo -e "\n### Load Testing ###\n" >> $RESULT_FILE
for c in "${CONCURRENT_USERS[@]}"; do
  echo "Testing with $c concurrent users..." | tee -a $RESULT_FILE
  ab -n 500 -c $c -p $POST_FILE -T 'application/json' $API_URL >> $RESULT_FILE 2>&1
  echo -e "\n" >> $RESULT_FILE
done

# Test 2: Stress Testing
echo -e "\n### Stress Testing ###\n" >> $RESULT_FILE
echo "Testing with 1000 requests and 200 concurrent users..." | tee -a $RESULT_FILE
ab -n 1000 -c 200 -p $POST_FILE -T 'application/json' $API_URL >> $RESULT_FILE 2>&1
echo -e "\n" >> $RESULT_FILE

# Test 3: Latency Testing
echo -e "\n### Latency Testing ###\n" >> $RESULT_FILE
echo "Measuring latency with 1 request at a time..." | tee -a $RESULT_FILE
ab -n 10 -c 1 -p $POST_FILE -T 'application/json' $API_URL >> $RESULT_FILE 2>&1
echo -e "\n" >> $RESULT_FILE

# Test 4: Concurrency Testing
echo -e "\n### Concurrency Testing ###\n" >> $RESULT_FILE
for c in "${CONCURRENT_USERS[@]}"; do
  echo "Testing with $c concurrent users..." | tee -a $RESULT_FILE
  ab -n 1000 -c $c -p $POST_FILE -T 'application/json' $API_URL >> $RESULT_FILE 2>&1
  echo -e "\n" >> $RESULT_FILE
done

# Test 5: Throughput Testing
echo -e "\n### Throughput Testing ###\n" >> $RESULT_FILE
echo "Measuring throughput with 5000 requests and 100 concurrent users..." | tee -a $RESULT_FILE
ab -n 5000 -c 100 -p $POST_FILE -T 'application/json' $API_URL >> $RESULT_FILE 2>&1
echo -e "\n" >> $RESULT_FILE

# Completion message
echo -e "\nPerformance Tests Completed. Results saved to $RESULT_FILE"


