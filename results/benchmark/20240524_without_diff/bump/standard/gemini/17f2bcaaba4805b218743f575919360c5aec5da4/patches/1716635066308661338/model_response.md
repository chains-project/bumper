```java
package org.junit;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * Indicates that a test method should be run only if a certain condition is true.
 * If the condition is false, the test method will not be executed.
 * <p>
 * This annotation can be used on test methods, test classes, or individual test cases within a test
 * class.
 * <p>
 * The condition to be evaluated can be specified using a {@link String} expression, a
 * {@link Class} literal, or a {@link ClassValue}.
 * <p>
 * If a {@link String} expression is used, it will be evaluated using the
 * {@link org.junit.Assume} class.
 * <p>
 * If a {@link Class} literal is used, the test will only be run if the current JVM supports that
 * class.
 * <p>
 * If a {@link ClassValue} is used, the test will only be run if the value returned by the
 * {@link ClassValue} is not null.
 * <p>
 * Example usage:
 * <pre>
 * public class MyTest {
 *
 *     &#064;Test
 *     public void testOnlyOnJava8() {
 *         assumeTrue(JavaVersion.current().isJava8Compatible());
 *         // ...
 *     }
 * }
 * </pre>
 *
 * @since 4.7
 */
@Retention(RetentionPolicy.RUNTIME)
@Target({ElementType.METHOD, ElementType.TYPE})
public @interface Assume {

    /**
     * The condition to be evaluated.
     *
     * @return the condition to be evaluated
     */
    String value();
}
```