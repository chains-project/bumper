```java
private Matcher<String> manifestPushed() {
    String pattern = String.format("latest: digest: %s", this.image.digest());
    return Matchers.containsString(pattern);
}
```