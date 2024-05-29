Here is a fixed version of the code that should resolve the error:

```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.CoreMatchers.containsString(java.lang.String.format("%s: Pushed", this.image.layer()));
}
```

In the original code, you were using the `StringContains` constructor which takes a boolean and a string as arguments. However, the error message indicates that the constructor you intended to use is the one that takes a single string argument.

To fix the error, I replaced the `StringContains` constructor with the `containsString` method from the `CoreMatchers` class, which takes a single string argument and checks if it contains the specified substring. This should resolve the error and allow the code to compile successfully.