```java
private Matcher<String> manifestPushed() {
    // -- String.format
    // ++ String.format(Locale.getDefault(), "latest: digest: %s", this.image.digest())
    return new StringContains(false, String.format(Locale.getDefault(), "latest: digest: %s", this.image.digest()));
}
```