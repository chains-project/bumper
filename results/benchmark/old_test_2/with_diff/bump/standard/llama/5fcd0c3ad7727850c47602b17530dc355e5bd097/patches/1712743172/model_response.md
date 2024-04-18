Here's a possible patch to fix the error:
```java
private org.pitest.elements.models.MutationTestSummaryData createSummaryData(final org.pitest.coverage.CoverageDatabase coverage, final org.pitest.mutationtest.ClassMutationResults data) {
    return new org.pitest.elements.models.MutationTestSummaryData(data.getFileName(), data.getMutations(), coverage.getClassInfo(data.getMutatedClass().getName()));
}
```
The patch replaces the line:
```java
coverage.getClassInfo(java.util.Collections.singleton(data.getMutatedClass()));
```
with:
```java
coverage.getClassInfo(data.getMutatedClass().getName());
```
The `getClassInfo()` method has been removed from the `CoverageDatabase` interface, so we need to use the `getName()` method of the `ClassName` object to get the name of the class, and then pass that name to the `getClassInfo()` method of the `CoverageDatabase` object.

This patch should fix the error and allow the code to compile again.