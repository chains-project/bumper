Here's the patched method using the new library version:
```java
private org.hamcrest.Matcher<String> manifestPushed() {
    return new org.hamcrest.core.StringStartsWith(String.format("latest: digest: %s", this.image.digest()));
}
```
The `StringContains` constructor no longer accepts a boolean parameter, so we've replaced it with `StringStartsWith` which accepts a single String argument.