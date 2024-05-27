Here is the patched code:

```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.CoreMatchers.not(org.hamcrest.CoreMatchers.stringContains(String.format("%s: Pushed", this.image.layer())));
}
```

The original code used static imports for `IsNot` and `StringContains` from `org.hamcrest.core` package. However, the new version of the library has removed these classes and replaced them with static methods in `org.hamcrest.CoreMatchers` class. Therefore, I have replaced the original imports with the new ones and used the new static methods.