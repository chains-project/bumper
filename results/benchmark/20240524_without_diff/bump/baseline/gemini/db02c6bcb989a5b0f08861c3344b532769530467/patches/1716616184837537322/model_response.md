```java
  private Matcher<String> manifestPushed() {
        return new StringContains(false, "latest: digest: " + this.image.digest());
    }
```