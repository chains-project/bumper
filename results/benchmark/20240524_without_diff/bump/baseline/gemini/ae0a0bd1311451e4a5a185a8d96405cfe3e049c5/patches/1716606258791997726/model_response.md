```java
private Matcher<String> manifestPushed() {
    return new StringContains(false, String.format("latest: digest: %s", this.image.digest));
}
```