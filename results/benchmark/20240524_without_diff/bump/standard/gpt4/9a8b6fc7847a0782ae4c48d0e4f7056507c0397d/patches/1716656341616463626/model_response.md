It seems like the library `org.jasypt.spring.security` has been removed or is not available in your classpath. If you're using a version of Jasypt where the `PBEPasswordEncoder` class has been moved to a different package, you should update the import statement accordingly. 

If the class has been moved to the `org.jasypt.spring5.security3` package in a newer version of Jasypt, you should change the import statement to:

```java
import org.jasypt.spring5.security3.PBEPasswordEncoder;
```