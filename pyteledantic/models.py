from datetime import datetime
from typing import Optional, Union, List

from pydantic import BaseModel, Field, validator


class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    language_code: Optional[str] = None
    can_join_groups: Optional[bool] = None
    can_read_all_group_messages: Optional[bool] = None
    supports_inline_queries: Optional[bool] = None


class ChatPhoto(BaseModel):
    small_file_id: str
    small_file_unique_id: str
    big_file_id: str
    big_file_unique_id: str


class ChatPermissions(BaseModel):
    can_send_messages: Optional[bool] = None
    can_send_media_messages: Optional[bool] = None
    can_send_polls: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None
    can_change_info: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_pin_messages: Optional[bool] = None


class Location(BaseModel):
    longitude: float
    latitude: float
    horizontal_accuracy: Optional[float] = None
    live_period: Optional[int] = None
    heading: Optional[int] = None
    proximity_alert_radius: Optional[int] = None

    @validator('horizontal_accuracy')
    def size_horizontal_accuracy_must_contain_a_range(self, value):
        if value < 0 or value > 1500:
            raise ValueError('Must contain a range of 0 - 1500')


class ChatLocation(BaseModel):
    location: Location
    address: str


class Chat(BaseModel):
    id: int
    type: str
    title: Optional[str] = None
    username: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    photo: Optional[ChatPhoto] = None
    bio: Optional[str] = None
    description: Optional[str] = None
    invite_link: Optional[str] = None
    pinned_message: Optional['Message'] = None
    permissions: Optional[ChatPermissions] = None
    slow_mode_delay: Optional[int] = None
    message_auto_delete_time: Optional[int] = None
    sticker_set_name: Optional[str] = None
    can_set_sticker_set: Optional[bool] = None
    linked_chat_id: Optional[int] = None
    location: Optional[ChatLocation] = None


class MessageEntity(BaseModel):
    type: str
    offset: int
    length: int
    url: Optional[str] = None
    user: Optional[User] = None
    language: Optional[str] = None


class PhotoSize(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    file_size: Optional[int] = None


class Animation(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


class Audio(BaseModel):
    file_id: str
    file_unique_id: str
    duration: int
    performer: Optional[str] = None
    title: Optional[str] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None
    thumb: Optional[PhotoSize] = None


class Document(BaseModel):
    file_id: str
    file_unique_id: str
    thumb: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


class Sticker(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    is_animated: bool
    thumb: Optional[PhotoSize] = None
    emoji: Optional[str] = None
    set_name: Optional[str] = None
    mask_position: Optional[str] = None
    file_size: Optional[int] = None


class Video(BaseModel):
    file_id: str
    file_unique_id: str
    width: int
    height: int
    duration: int
    thumb: Optional[PhotoSize] = None
    file_name: Optional[str] = None
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


class VideoNote(BaseModel):
    file_id: str
    file_unique_id: str
    length: int
    duration: int
    thumb: Optional[PhotoSize] = None
    file_size: Optional[int] = None


class Voice(BaseModel):
    file_id: str
    file_unique_id: str
    duration: int
    mime_type: Optional[str] = None
    file_size: Optional[int] = None


class Contact(BaseModel):
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    user_id: Optional[str] = None
    vcard: Optional[str] = None


class Dice(BaseModel):
    emoji: str
    value: int


class Game(BaseModel):
    title: str
    description: str
    photo: Union[list, PhotoSize, None] = None
    text: Optional[str] = None
    text_entities: Union[list, MessageEntity, None] = None
    animation: Optional[Animation] = None


class PollOption(BaseModel):
    text: str
    voter_count: int


class Poll(BaseModel):
    id: str
    question: str
    options: Union[list, PollOption, None] = None
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: Optional[int] = None
    explanation: Optional[str] = None
    explanation_entities: Union[list, MessageEntity, None] = None
    open_period: Optional[int] = None
    close_date: Optional[int] = None

    @validator('question')
    def question_characters_limit(self, value):
        if len(value) > 300:
            raise ValueError('question limited 300 characters')


class MessageAutoDeleteTimerChanged(BaseModel):
    message_auto_delete_time: int


class Venue(BaseModel):
    location: Location
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    google_place_id: Optional[str] = None
    google_place_type: Optional[str] = None


class Invoice(BaseModel):
    title: str
    description: str
    start_parameter: str
    currency: str
    total_amount: int


class ShippingAddress(BaseModel):
    country_code: str
    state: str
    city: str
    street_line1: str
    street_line2: str
    post_code: str


class OrderInfo(BaseModel):
    name: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    shipping_address: Optional[ShippingAddress] = None


class SuccessfulPayment(BaseModel):
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None
    telegram_payment_charge_id: str
    provider_payment_charge_id: str


class PassportFile(BaseModel):
    file_id: str
    file_unique_id: str
    file_size: int
    file_date: int


class EncryptedPassportElement(BaseModel):
    type: str
    data: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    files: Union[list, PassportFile, None] = None
    front_side: Optional[PassportFile] = None
    reverse_side: Optional[PassportFile] = None
    selfie: Optional[PassportFile] = None
    translation: Union[list, PassportFile, None] = None
    hash: str


class EncryptedCredentials(BaseModel):
    data: str
    hash: str
    secret: str


class PassportData(BaseModel):
    data: Union[list, EncryptedPassportElement]
    credentials: EncryptedCredentials


class ProximityAlertTriggered(BaseModel):
    traveler: User
    watcher: User
    distance: int


class VoiceChatScheduled(BaseModel):
    start_date: int


class VoiceChatStarted(BaseModel):
    pass


class VoiceChatEnded(BaseModel):
    duration: int


class VoiceChatParticipantsInvited(BaseModel):
    users: Union[list, User, None] = None


class LoginUrl(BaseModel):
    url: str
    forward_text: Optional[str] = None
    bot_username: Optional[str] = None
    request_write_access: Optional[bool] = None


class CallbackGame(BaseModel):
    pass


class InlineKeyboardButton(BaseModel):
    text: str
    url: Optional[str]
    login_url: Optional[LoginUrl] = None
    callback_data: Optional[str] = None
    switch_inline_query: Optional[str] = None
    switch_inline_query_current_chat: Optional[str] = None
    callback_game: Optional[CallbackGame] = None
    pay: Optional[bool]


class InlineKeyboardMarkup(BaseModel):
    inline_keyboard: Union[list, List[InlineKeyboardButton]]


class Message(BaseModel):
    message_id: int
    from_user: Optional[User] = Field(None, alias='from')
    sender_chat: Optional[Chat] = None
    date: datetime
    chat: Chat
    forward_from: Optional[User] = None
    forward_from_chat: Optional[Chat] = None
    forward_from_message_id: Optional[int] = None
    forward_signature: Optional[str] = None
    forward_sender_name: Optional[str] = None
    forward_date: Optional[int] = None
    reply_to_message: Optional['Message'] = None
    via_bot: Optional[User] = None
    edit_date: Optional[int] = None
    media_group_id: Optional[str] = None
    author_signature: Optional[str] = None
    text: Optional[str] = None
    entities: Union[list, MessageEntity, None] = None
    animation: Optional[Animation] = None
    audio: Optional[Audio] = None
    document: Optional[Document] = None
    photo: Union[list, PhotoSize, None] = None
    sticker: Optional[Sticker] = None
    video: Optional[Video] = None
    video_note: Optional[VideoNote] = None
    voice: Optional[Voice] = None
    caption: Optional[str] = None
    caption_entities: Union[list, MessageEntity, None] = None
    contact: Optional[Contact] = None
    dice: Optional[Dice] = None
    game: Optional[Game] = None
    poll: Optional[Poll] = None
    venue: Optional[Venue] = None
    location: Optional[Location] = None
    new_chat_members: Optional[list, User, None] = None
    left_chat_member: Optional[User] = None
    new_chat_title: Optional[str] = None
    new_chat_photo: Optional[list, PhotoSize, None] = None
    delete_chat_photo: Optional[bool] = None
    group_chat_created: Optional[bool] = None
    supergroup_chat_created: Optional[bool] = None
    channel_chat_created: Optional[bool] = None
    message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = None
    migrate_to_chat_id: Optional[int] = None
    migrate_from_chat_id: Optional[int] = None
    pinned_message: Optional['Message'] = None
    invoice: Optional[Invoice] = None
    successful_payment: Optional[SuccessfulPayment] = None
    connected_website: Optional[str] = None
    passport_data: Optional[PassportData] = None
    proximity_alert_triggered: Optional[ProximityAlertTriggered] = None
    voice_chat_scheduled: Optional[VoiceChatScheduled] = None
    voice_chat_started: Optional[VoiceChatStarted] = None
    voice_chat_ended: Optional[VoiceChatEnded] = None
    voice_chat_participants_invited: Optional[VoiceChatParticipantsInvited] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


class InlineQuery(BaseModel):
    id: str
    from_user: User = Field(alias='from')
    query: str
    offset: str
    chat_type: Optional[str] = None
    location: Optional[Location] = None

    @validator('query')
    def query_characters_limit(self, value):
        if len(value) > 256:
            raise ValueError('query limited 256 characters')


class ChosenInlineResult(BaseModel):
    result_id: str
    from_user: User = Field(alias='from')
    location: Optional[Location] = None
    inline_message_id: Optional[str] = None
    query: str


class CallbackQuery(BaseModel):
    id: str
    from_user: User = Field(alias='from')
    message: Optional[Message] = None
    inline_message_id: Optional[str] = None
    chat_instance: str
    data: Optional[str] = None
    game_short_name: Optional[str] = None


class ShippingQuery(BaseModel):
    id: str
    from_user: User = Field(alias='from')
    invoice_payload: str
    shipping_address: ShippingAddress


class PreCheckoutQuery(BaseModel):
    id: str
    from_user: User = Field(alias='from')
    currency: str
    total_amount: int
    invoice_payload: str
    shipping_option_id: Optional[str] = None
    order_info: Optional[OrderInfo] = None


class PollAnswer(BaseModel):
    poll_id: str
    user: User
    option_ids: Union[list, int]


class ChatMemberOwner(BaseModel):
    status: str
    user: User
    is_anonymous: bool
    custom_title: Optional[str] = None


class ChatMemberAdministrator(BaseModel):
    status: str
    user: User
    can_be_edited: bool
    is_anonymous: bool
    can_manage_chat: bool
    can_delete_messages: bool
    can_manage_voice_chats: bool
    can_restrict_members: bool
    can_promote_members: bool
    can_change_info: bool
    can_invite_users: bool
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    custom_title: Optional[str] = None


class ChatMemberMember(BaseModel):
    status: str
    user: User


class ChatMemberRestricted(BaseModel):
    status: str
    user: User
    is_member: bool
    can_change_info: bool
    can_invite_users: bool
    can_pin_messages: bool
    can_send_messages: bool
    can_send_media_messages: bool
    can_send_polls: bool
    can_send_other_messages: bool
    can_add_web_page_previews: bool
    until_date: datetime


class ChatMemberLeft(BaseModel):
    status: str
    user: User


class ChatMemberBanned(BaseModel):
    status: str
    user: User
    until_date: int


class ChatInviteLink(BaseModel):
    invite_link: str
    creator: User
    is_primary: bool
    is_revoked: bool
    expire_date: Optional[int] = None
    member_limit: Optional[int] = None


class ChatMemberUpdated(BaseModel):
    chat: Chat
    from_user: User = Field(alias='from')
    date: datetime
    old_chat_member: Union[
        ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft,
        ChatMemberBanned]
    new_chat_member: Union[
        ChatMemberOwner, ChatMemberAdministrator, ChatMemberMember, ChatMemberRestricted, ChatMemberLeft,
        ChatMemberBanned]
    invite_link: ChatInviteLink


class Update(BaseModel):
    update_id: int
    message: Optional[Message] = None
    edited_message: Optional[Message] = None
    channel_post: Optional[Message] = None
    edited_channel_post: Optional[Message] = None
    inline_query: Optional[InlineQuery] = None
    chosen_inline_result: Optional[ChosenInlineResult] = None
    callback_query: Optional[CallbackQuery] = None
    shipping_query: Optional[ShippingQuery] = None
    pre_checkout_query: Optional[PreCheckoutQuery] = None
    poll: Optional[Poll] = None
    poll_answer: Optional[PollAnswer] = None
    my_chat_member: Optional[ChatMemberUpdated] = None
    chat_member: Optional[ChatMemberUpdated] = None
