Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(data.getMutatedClass().getName()));
}
```
The patch replaces the following line:
```java
coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));
```
with:
```java
coverage.getClassInfo(data.getMutatedClass().getName());
```
The `getClassInfo` method takes a `ClassName` parameter, which is a `java.util.Set` of class names. However, the `ClassName` parameter is not a `java.util.Set` but a `java.lang.String` representing the fully qualified name of the class.

The patch fixes the error by passing the fully qualified name of the mutated class instead of a set containing the class.