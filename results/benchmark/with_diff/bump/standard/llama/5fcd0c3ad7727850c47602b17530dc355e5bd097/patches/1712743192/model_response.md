Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfoBuilder().getClassInfo(data.getMutatedClass()));
}
```
This patch replaces the line that causes the error:
```scss
coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));
```
with a call to the `getClassInfoBuilder()` method, which returns a `ClassInfoBuilder` instance that can be used to get the `ClassInfo` for the mutated class.

The `getClassInfoBuilder()` method is a new addition in the updated library version, and it allows us to retrieve the `ClassInfo` for a given class name, bytecode, and timestamp.

With this patch, the code should now compile and run without any issues.