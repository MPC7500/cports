#!/bin/sh
IDEA_HOME="/usr/share/intellij-idea-community"
export JAVA_HOME="$IDEA_HOME/jbr"
export PATH="$JAVA_HOME/bin:$PATH"
exec "$IDEA_HOME/bin/idea.sh" "$@"