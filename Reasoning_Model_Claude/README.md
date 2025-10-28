# Claude 3.7 Sonnet Reasoning with Amazon Bedrock

This guide demonstrates how to use Anthropic Claude 3.7 Sonnet's reasoning capability with Amazon Bedrock using Python.

## Reference
- [How to use reasoning with Claude 3.7 Sonnet on Amazon Bedrock (Python Edition)](https://builder.aws.com/content/2tWvN7GNtVuBco4fNgLuowHas2c/how-to-use-reasoning-with-claude-37-sonnet-on-amazon-bedrock-python-edition)

## Prerequisites

Install required packages:
```bash
pip install boto3 python-dotenv
```

## AWS Credentials Setup

This notebook uses a `.env` file to manage AWS credentials.

### Setup Instructions:

1. Create a `.env` file in the project root directory
2. Copy the content below and paste it into the `.env` file, then replace with your actual values:

```env
AWS_ACCESS_KEY_ID=your-access-key-id-here
AWS_SECRET_ACCESS_KEY=your-secret-access-key-here
AWS_DEFAULT_REGION=us-east-1
```

### Important:
- **Never commit the `.env` file to git!**
- Make sure `.env` is included in your `.gitignore` file

---

## Step-by-Step Implementation Guide

### Step 1: Create a Basic File Structure

Create a new Python file (e.g., `claude_reasoning.py`) where we'll implement our code to interact with Claude's reasoning capability:

```python
import boto3
from botocore.exceptions import ClientError

def reasoning_example():
    # We'll implement this function in the next steps
    pass

if __name__ == "__main__":
    # We'll call our reasoning function here
    pass
```

### Step 2: Set Up the Amazon Bedrock Client

First, we need to create a Bedrock runtime client that will handle our API requests. Add the following to the `reasoning_example()` function:

```python
# Create the Amazon Bedrock runtime client
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Specify the model ID for Claude 3.7 Sonnet
model_id = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"
```

### Step 3: Create a Message for Claude

Next, we'll create a simple message to send to Claude:

```python
# Create the message with the user's prompt
user_message = "What is the purpose of a hello world program?"
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]
```

### Step 4: Configure Reasoning Parameters

Here's where the magic happens - we need to enable reasoning and set a token budget for it:

```python
# Configure reasoning parameters with a 2000 token budget
reasoning_config = {
    "thinking": {
        "type": "enabled",
        "budget_tokens": 2000
    }
}
```

### Step 5: Send the Request to Claude

Now we'll send our prompt along with the reasoning configuration:

```python
# Send message and reasoning configuration to the model
response = client.converse(
    modelId=model_id,
    messages=conversation,
    additionalModelRequestFields=reasoning_config
)
```

**Note:** The `additionalModelRequestFields` parameter is what allows us to pass the reasoning configuration.

### Step 6: Process the Response

Claude will return both its reasoning and final response, which we need to extract:

```python
# Extract the list of content blocks from the model's response
content_blocks = response["output"]["message"]["content"]

reasoning = None
text = None

# Process each content block to find reasoning and response text
for block in content_blocks:
    if "reasoningContent" in block:
        reasoning = block["reasoningContent"]["reasoningText"]["text"]
    if "text" in block:
        text = block["text"]

return reasoning, text
```

### Step 7: Display the Results

Finally, we'll display both the reasoning process and the final answer. Update your main function:

```python
if __name__ == "__main__":
    # Execute the example and display reasoning and final response
    reasoning, text = reasoning_example()
    print("\n<thinking>")
    print(reasoning)
    print("</thinking>\n")
    print(text)
```

---

## Example Output

When you run this code, you'll see output similar to:

```
================================================================================
REASONING PROCESS (Thinking)
================================================================================
This question asks about enterprise business problems that can be solved by building AI agents with reasoning models. Let me explore several domains and applications where such agents could be valuable:

1. Customer Service and Support
   - Handling complex customer inquiries that require reasoning across multiple knowledge bases
   - Troubleshooting technical issues by reasoning through potential causes and solutions
   - Creating personalized recommendations based on customer history and preferences

2. Knowledge Management
   - Synthesizing information across large document repositories
   - Answering complex questions that require integrating multiple information sources
   - Maintaining and updating knowledge bases by identifying inconsistencies or gaps

3. Decision Support
   - Helping with complex business decisions by analyzing pros and cons
   - Risk assessment that requires evaluating multiple factors
   - Strategic planning that involves reasoning about competitors, market trends, etc.

4. Operations and Supply Chain
   - Optimizing complex supply chain decisions
   - Identifying root causes of operational inefficiencies
   - Managing resource allocation across competing priorities

5. Legal and Compliance
   - Contract analysis and risk identification
   - Regulatory compliance monitoring and reporting
   - Legal research and case preparation assistance

6. Finance
   - Complex financial analysis and modeling
   - Fraud detection through pattern recognition and anomaly analysis
   - Investment strategy optimization

7. Human Resources
   - Sophisticated candidate matching for specialized roles
   - Performance management through multi-factor analysis
   - Learning and development path customization

8. Product Development
   - Market research synthesis and product opportunity identification
   - Feature prioritization based on complex criteria
   - Customer feedback analysis and interpretation

9. Sales and Marketing
   - Lead qualification that requires reasoning about prospect fit
   - Content personalization based on user behavior and preferences
   - Campaign optimization across multiple channels

10. IT and Security
    - Troubleshooting complex system issues
    - Security threat analysis and response planning
    - Infrastructure optimization decisions

For each of these areas, reasoning models allow AI agents to:
- Handle ambiguity and uncertainty
- Make decisions with incomplete information
- Apply domain knowledge to novel situations
- Follow multi-step logical processes
- Explain their recommendations in human-understandable terms

I should emphasize that these applications specifically benefit from reasoning capabilities beyond what traditional ML systems can do, as they involve complex decision-making processes rather than simple pattern recognition.

================================================================================
FINAL RESPONSE
================================================================================
# Enterprise Business Problems Solvable with Reasoning-Based Agents

Reasoning models enable AI agents to perform complex multi-step thinking, handle ambiguity, and provide explanations for their conclusions. Here are key enterprise applications:

## Knowledge Work Automation
- **Contract Analysis:** Extracting obligations, risks, and unusual terms while explaining legal implications
- **Financial Analysis:** Interpreting complex financial statements and identifying discrepancies or opportunities
- **Research Synthesis:** Consolidating findings across multiple documents and drawing actionable conclusions

## Complex Decision Support
- **Strategic Planning:** Evaluating different scenarios while considering multiple business constraints
- **Risk Assessment:** Identifying potential problems across operations with clear reasoning paths
- **Resource Allocation:** Optimizing staff and budget distribution with transparent justification

## Operational Intelligence
- **Root Cause Analysis:** Diagnosing issues in complex systems through logical reasoning
- **Supply Chain Optimization:** Identifying inefficiencies and suggesting improvements with explanations
- **Process Improvement:** Analyzing workflows to detect bottlenecks and recommend solutions

## Customer Engagement
- **Advanced Customer Support:** Solving complex, multi-step customer problems beyond simple FAQs
- **Personalized Recommendations:** Providing tailored advice with clear reasoning behind suggestions
- **Sales Enablement:** Supporting complex B2B sales processes requiring deep product knowledge

## Specialized Applications
- **Regulatory Compliance:** Interpreting complex regulations and ensuring business alignment
- **Product Development:** Reasoning through feature trade-offs and technical constraints
- **Knowledge Management:** Maintaining consistency across company information resources

The key advantage of reasoning agents is their ability to tackle problems requiring multi-step thinking, explain their conclusions, and adapt to new information—capabilities essential for high-value business applications.
================================================================================
```

---

## Summary and Next Steps

The reasoning capability transforms how we interact with AI by providing valuable insight into the model's thinking process. By following the steps in this guide, you can now access and leverage this powerful feature through Amazon Bedrock using Python.

The reasoning feature opens up exciting possibilities to enhance trust, improve outcomes, and gain deeper insights from your AI interactions.

### For More Advanced Use Cases, Consider:

- **Adjusting the token budget** based on your problem complexity – more complex problems may benefit from larger reasoning budgets
- **Using the reasoning output** to validate multi-step calculations or complex analytical processes
- **Comparing different reasoning approaches** by adjusting your prompts
- **Integrating reasoning** with other Claude capabilities like function calling for powerful, transparent AI solutions
- **Using reasoning as an educational tool** to understand expert-level problem-solving approaches

By incorporating reasoning into your applications, you're not just getting answers – you're gaining insight into the full problem-solving journey. This transparency can help build trust with users and provide richer, more valuable AI interactions.

