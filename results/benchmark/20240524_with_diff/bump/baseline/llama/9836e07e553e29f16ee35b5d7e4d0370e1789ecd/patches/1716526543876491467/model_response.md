```java
private Matcher<String> manifestPushed() {
    String matcherString = String.format("latest: digest: %s", this.image.digest());
    return Matchers.containsString(matcherString);
}
```