```java
private Matcher<String> manifestPushed() {
    String expectedString = String.format("latest: digest: %s", this.image.digest());
    return Matchers.containsString(expectedString);
}
```