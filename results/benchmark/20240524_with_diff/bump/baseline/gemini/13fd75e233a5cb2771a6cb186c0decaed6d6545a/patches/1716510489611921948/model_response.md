```java
  private Matcher<String> manifestPushed() {
        String digest = this.image.digest();
        return new StringContains(false, "latest: digest: " + digest);
    }
```