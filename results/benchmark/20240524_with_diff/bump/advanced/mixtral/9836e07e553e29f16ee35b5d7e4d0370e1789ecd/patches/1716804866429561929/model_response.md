Here is the proposed patch:

```java
private org.hamcrest.Matcher<java.lang.String> layersAlreadyExist() {
    return org.hamcrest.CoreMatchers.containsString(java.lang.String.format("%s: Layer already exists", this.image.layer()));
}
```

The change is to use the `containsString` method from `CoreMatchers` instead of `StringContains`. This method only takes a single `String` argument, which matches the signature of the constructor.