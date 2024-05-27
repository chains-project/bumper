Here is the fixed `layersPushed()` method:

```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.CoreMatchers.not(org.hamcrest.CoreMatchers.stringContains(String.format("%s: Pushed", this.image.layer())));
}
```

The error is caused by the removal of the core matchers from the `org.hamcrest` package. Instead of creating new instances of `IsNot` and `StringContains`, you can now use the static methods `not` and `stringContains` from `CoreMatchers`. This way, you can avoid the dependency update issue and the code will still work with the new library version.