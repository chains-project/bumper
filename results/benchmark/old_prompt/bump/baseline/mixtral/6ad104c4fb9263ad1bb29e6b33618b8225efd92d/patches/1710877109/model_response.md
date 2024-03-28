Based on the information you've provided, it seems that the error message is indicating a syntax error in the line:
```java
import org.bouncycastle.jce.provider.JceTls;
```
However, the code snippet you've provided is just an import statement, which doesn't contain any syntax errors. Therefore, it's possible that the actual error is located in the `ChachaDecoder` class, particularly at line 23.

Without seeing the full codebase, it's difficult to provide a specific solution. However, based on the error message, it seems like there might be a missing semicolon (`;`) at the end of a statement. Here's a possible patch that might solve the issue:

```java
if (someCondition) {
  // some code here
}
// add a semicolon at the end of the if statement
```

Please note that this is just a general suggestion, and the actual solution may vary depending on the specific codebase. I would recommend reviewing the `ChachaDecoder` class, particularly at line 23, to identify the root cause of the error.