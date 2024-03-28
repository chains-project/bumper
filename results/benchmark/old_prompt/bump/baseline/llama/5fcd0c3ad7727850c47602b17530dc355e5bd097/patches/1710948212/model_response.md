Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(data.getMutatedClass())));
}
```

Add import statement for `org.pitest.coverage.CoverageDatabase` and remove the `Override` annotation:
```java
import org.pitest.coverage.CoverageDatabase;

private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), coverage.getClassInfo(Collections.singleton(data.getMutatedClass())));
}
```
The error message indicates that the `CoverageDatabase` class cannot be found, which suggests that the `pitest-mutation-testing-elements-plugin` dependency is not being used correctly. By adding the import statement, we ensure that the `CoverageDatabase` class is properly imported from the `org.pitest.coverage` package.

Additionally, the `Override` annotation is removed since it's not necessary in this case, and the method doesn't override any method in the superclass.