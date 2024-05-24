```java
private Matcher<String> layersPushed() {
        boolean isNegative = false;
        String layer = this.image.layer();
        String message = String.format("%s: Pushed", layer);
        if (message.startsWith("!")) {
            isNegative = true;
            message = message.substring(1);
        }
        return new StringContains(isNegative, message);
    }
```