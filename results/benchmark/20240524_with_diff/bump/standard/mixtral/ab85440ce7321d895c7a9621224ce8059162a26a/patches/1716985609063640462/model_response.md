Here is a patch that you can apply to the failing client code:
```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return org.hamcrest.Matchers.containsString(String.format("latest: digest: %s", this.image.digest()));
}
```
In the new version of the library, the `StringContains` constructor has been removed and replaced with the `containsString` method. The `containsString` method takes a single argument, which is the substring to search for in the target string. In this case, we are using the `String.format` method to construct the target string, which includes the image digest.