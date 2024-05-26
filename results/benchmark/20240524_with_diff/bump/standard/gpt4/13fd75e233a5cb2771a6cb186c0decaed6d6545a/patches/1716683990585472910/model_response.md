```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return org.hamcrest.core.StringContains.containsString(java.lang.String.format("latest: digest: %s", this.image.digest()));
}
```