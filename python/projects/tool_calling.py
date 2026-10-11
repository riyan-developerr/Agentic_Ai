import json

def run_tool(call_text, tools):
    """this function inputs user query and tools and give output accordingly"""
    
    # exception handling for invalid json
    try:
        call_obj = json.loads(call_text)
    except (json.JSONDecodeError,TypeError):
        return {"ok":False , "error":"Invalid JSON"}
    
    # exception handling for input other than object(dictionary)
    if not isinstance(call_obj, dict):
        return {"ok":False , "error":"Invalid object"}
        
    tool = call_obj.get("tool",None)
    if not isinstance(tool, str):
        return {"ok":False , "error":"Missing tool name"}
        
    
    # missing tool key error
    if tool not in tools:
        return {"ok":False , "error":f"unkown tool:{tool}"}
    
    args =  call_obj.get("args",{})
    if not isinstance(args, dict):
        return {"ok":False, "error":"args must be an object"}
    
    # getting tool from tools collection
    tool_fun = tools[tool]
    # inputs = tuple([arg for arg in args.values()])
    
    # invalid, bad, zero input error handling
    try:
        result = tool_fun(**args)
    except TypeError:
        return {"ok":False , "error":"Bad argument"}
    except ZeroDivisionError:
        return {"ok":False , "error":"Cannot divide by zero"} 
    except AttributeError: 
        return {"ok":False , "error":"Attribute error"} 
    except Exception as e:
        return {"ok":False, "error":f"tool failed:{e}"}
    
    return {"ok":True , "result":result}
    
        