from .view.MessageListView import MessageListView
from .view.MessageCreateView import MessageCreateView
Message_List = MessageListView.as_view()
Message_Create = MessageCreateView.as_view()