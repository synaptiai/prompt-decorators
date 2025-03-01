# Integration Examples

This document demonstrates how to integrate the Prompt Decorators core package with different platforms and frameworks.

## JavaScript/TypeScript Integration

### Node.js API Server

```javascript
// Import the core decorators
import { 
  Reasoning, 
  StepByStep, 
  OutputFormat, 
  Tone, 
  Version 
} from 'prompt-decorators-core';

// Express middleware for handling decorators
function decoratorMiddleware(req, res, next) {
  const { prompt, decorators = [] } = req.body;
  
  // Convert string decorators to objects if needed
  const decoratorObjects = decorators.map(d => {
    if (typeof d === 'string') {
      // Parse decorator string (+++Name(param=value))
      return parseDecoratorString(d);
    }
    return d;
  });
  
  // Add to request for later use
  req.decoratedPrompt = {
    prompt,
    decorators: decoratorObjects
  };
  
  next();
}

// API endpoint
app.post('/api/generate', decoratorMiddleware, async (req, res) => {
  const { prompt, decorators } = req.decoratedPrompt;
  
  // Convert decorators to system instructions
  const systemInstructions = convertDecoratorsToSystemInstructions(decorators);
  
  // Call LLM API with system instructions and prompt
  const response = await llmClient.generate({
    system: systemInstructions,
    prompt: prompt
  });
  
  res.json({ response });
});
```

### React Frontend Component

```jsx
import React, { useState } from 'react';
import { 
  DecoratorSelector, 
  DecoratorList 
} from 'prompt-decorators-react';

function AIPromptInterface() {
  const [prompt, setPrompt] = useState('');
  const [decorators, setDecorators] = useState([]);
  const [response, setResponse] = useState('');
  
  const addDecorator = (decorator) => {
    setDecorators([...decorators, decorator]);
  };
  
  const removeDecorator = (index) => {
    setDecorators(decorators.filter((_, i) => i !== index));
  };
  
  const handleSubmit = async () => {
    const response = await fetch('/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt, decorators })
    });
    
    const data = await response.json();
    setResponse(data.response);
  };
  
  return (
    <div className="ai-interface">
      <h2>AI Prompt with Decorators</h2>
      
      <DecoratorSelector onSelect={addDecorator} />
      
      <DecoratorList 
        decorators={decorators} 
        onRemove={removeDecorator} 
      />
      
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt here..."
      />
      
      <button onClick={handleSubmit}>Generate</button>
      
      <div className="response">
        <h3>Response:</h3>
        <div>{response}</div>
      </div>
    </div>
  );
}
```

## Python Integration

### FastAPI Backend

```python
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from prompt_decorators_core import (
    Reasoning,
    StepByStep,
    OutputFormat,
    Tone,
    Version,
    parse_decorator_string,
    convert_decorators_to_system_instructions
)

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str
    decorators: List[Dict[str, Any]] = []
    decorator_strings: Optional[List[str]] = None

class PromptResponse(BaseModel):
    response: str

@app.post("/api/generate", response_model=PromptResponse)
async def generate_response(request: PromptRequest):
    # Process decorator strings if provided
    if request.decorator_strings:
        parsed_decorators = [
            parse_decorator_string(d) for d in request.decorator_strings
        ]
        request.decorators.extend(parsed_decorators)
    
    # Convert decorators to system instructions
    system_instructions = convert_decorators_to_system_instructions(request.decorators)
    
    # Call LLM API
    response = await call_llm_api(
        system_instructions=system_instructions,
        prompt=request.prompt
    )
    
    return PromptResponse(response=response)

async def call_llm_api(system_instructions: str, prompt: str) -> str:
    # Implementation depends on your LLM provider
    # Example with OpenAI
    from openai import AsyncOpenAI
    
    client = AsyncOpenAI()
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
```

### Streamlit UI

```python
import streamlit as st
from prompt_decorators_core import (
    Reasoning,
    StepByStep,
    OutputFormat,
    Tone,
    Version,
    OutputFormat,
    ToneStyle
)
import requests

st.title("AI Prompt with Decorators")

# Decorator selection
st.header("Select Decorators")

with st.expander("Reasoning"):
    use_reasoning = st.checkbox("Use Reasoning Decorator")
    if use_reasoning:
        reasoning_depth = st.selectbox(
            "Depth",
            ["basic", "moderate", "comprehensive"],
            index=1
        )

with st.expander("Step by Step"):
    use_stepbystep = st.checkbox("Use StepByStep Decorator")
    if use_stepbystep:
        numbered = st.checkbox("Numbered Steps", value=True)

with st.expander("Output Format"):
    use_outputformat = st.checkbox("Use OutputFormat Decorator")
    if use_outputformat:
        format_option = st.selectbox(
            "Format",
            ["plaintext", "markdown", "json", "yaml", "xml"],
            index=0
        )

with st.expander("Tone"):
    use_tone = st.checkbox("Use Tone Decorator")
    if use_tone:
        tone_style = st.selectbox(
            "Style",
            ["formal", "casual", "friendly", "technical", "humorous"],
            index=0
        )

# Prompt input
st.header("Enter Prompt")
prompt = st.text_area("Prompt", height=150)

# Generate button
if st.button("Generate Response"):
    # Build decorators list
    decorators = []
    
    if use_reasoning:
        decorators.append({
            "name": "Reasoning",
            "version": "1.0.0",
            "parameters": {"depth": reasoning_depth}
        })
    
    if use_stepbystep:
        decorators.append({
            "name": "StepByStep",
            "version": "1.0.0",
            "parameters": {"numbered": numbered}
        })
    
    if use_outputformat:
        decorators.append({
            "name": "OutputFormat",
            "version": "1.0.0",
            "parameters": {"format": format_option}
        })
    
    if use_tone:
        decorators.append({
            "name": "Tone",
            "version": "1.0.0",
            "parameters": {"style": tone_style}
        })
    
    # Call API
    response = requests.post(
        "http://localhost:8000/api/generate",
        json={"prompt": prompt, "decorators": decorators}
    )
    
    if response.status_code == 200:
        st.header("Response")
        st.write(response.json()["response"])
    else:
        st.error(f"Error: {response.status_code}")
        st.error(response.text)
```

## Command Line Interface

### Node.js CLI

```javascript
#!/usr/bin/env node
import { program } from 'commander';
import { 
  Reasoning, 
  StepByStep, 
  OutputFormat, 
  Tone, 
  Version,
  convertDecoratorsToSystemInstructions
} from 'prompt-decorators-core';
import { Configuration, OpenAIApi } from 'openai';

program
  .name('prompt-decorate')
  .description('CLI for using prompt decorators')
  .version('1.0.0');

program
  .command('generate')
  .description('Generate a response using prompt decorators')
  .argument('<prompt>', 'The prompt text')
  .option('-r, --reasoning [depth]', 'Use Reasoning decorator with optional depth')
  .option('-s, --step-by-step [numbered]', 'Use StepByStep decorator with optional numbered flag')
  .option('-f, --format <format>', 'Use OutputFormat decorator with specified format')
  .option('-t, --tone <style>', 'Use Tone decorator with specified style')
  .option('-v, --version <version>', 'Use Version decorator with specified version')
  .action(async (prompt, options) => {
    const decorators = [];
    
    if (options.reasoning) {
      decorators.push(new Reasoning({
        depth: typeof options.reasoning === 'string' ? options.reasoning : 'moderate'
      }));
    }
    
    if (options.stepByStep) {
      decorators.push(new StepByStep({
        numbered: options.stepByStep === 'false' ? false : true
      }));
    }
    
    if (options.format) {
      decorators.push(new OutputFormat({
        format: options.format
      }));
    }
    
    if (options.tone) {
      decorators.push(new Tone({
        style: options.tone
      }));
    }
    
    if (options.version) {
      decorators.push(new Version({
        standard: options.version
      }));
    }
    
    const systemInstructions = convertDecoratorsToSystemInstructions(decorators);
    
    // Call OpenAI API
    const configuration = new Configuration({
      apiKey: process.env.OPENAI_API_KEY,
    });
    const openai = new OpenAIApi(configuration);
    
    try {
      const response = await openai.createChatCompletion({
        model: "gpt-4",
        messages: [
          { role: "system", content: systemInstructions },
          { role: "user", content: prompt }
        ],
      });
      
      console.log(response.data.choices[0].message.content);
    } catch (error) {
      console.error('Error:', error.message);
    }
  });

program.parse(); 