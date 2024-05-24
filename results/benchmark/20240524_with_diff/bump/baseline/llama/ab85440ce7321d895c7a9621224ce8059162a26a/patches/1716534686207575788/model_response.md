```java
private Matcher<String> manifestPushed() {
    String expected = String.format("latest: digest: %s", this.image.digest());
    return Matchers.containsString(expected);
}
```